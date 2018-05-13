use fnv::FnvHashMap;
use std::collections::{BTreeMap, BTreeSet};
use std::fs::File;
use std::io::Write;
use std::fs::create_dir;
use serde_json::to_string;

#[derive(Deserialize, Debug)]
pub struct Index {
    index: BTreeMap<String, BTreeMap<String, f64>>,
    movies: BTreeSet<String>,
    tokens: FnvHashMap<String, FnvHashMap<String, f64>>,
    names: FnvHashMap<String, String>,
    size: f64,
}

impl Index {

    pub fn new() -> Self {
        Index {
            index: BTreeMap::default(),
            movies: BTreeSet::default(),
            tokens: FnvHashMap::default(),
            names: FnvHashMap::default(),
            size: 0.0
        }
    }

    pub fn insert(&mut self, id: String, name: String, tokens: Vec<String>) {
        self.size += 1.0;
        self.movies.insert(id.clone());
        self.names.insert(id.clone(), name);

        let mut counter = FnvHashMap::default();

        for token in &tokens {
            let count = counter.entry(token.clone()).or_insert(0.0);
            *count += 1.0; 
        }
        self.tokens.insert(id.clone(), counter);

        for term in tokens {
            let mut posting = self.index.entry(term).or_insert(BTreeMap::default());
            let mut document = posting.entry(id.clone()).or_insert(0.0);
            *document += 1.0;
        }
    }

    pub fn process(&self) {
        let mut idfs: BTreeMap<String, f64> = BTreeMap::default();
        let mut norms: BTreeMap<String, f64> = BTreeMap::default();

        let (min, max) = (10, (0.75 * self.size) as usize);

        for (term, posting) in &self.index {
            if posting.len() < min || posting.len() > max { continue }
            idfs.insert(term.clone(), f64::log2(self.size / (posting.len() as f64)));
        }

        for (term, posting) in &self.index {
            if !idfs.contains_key(term) { continue }
            let idf = idfs[term];
            for (doc, count) in posting {
                let mut entry = norms.entry(doc.clone()).or_insert(0.0);
                *entry += ((1.0 + count.log2()) * idf).powi(2);
            }
        }

        for (_, norm) in &mut norms { *norm = norm.sqrt(); }
        
        let _ = create_dir("cosine");
        for (i, movie) in self.movies.iter().enumerate() {
            println!("{}", i);
            self.cosine(movie, &idfs, &norms);
        }
    }

    pub fn cosine(&self, movie: &str, idfs: &BTreeMap<String, f64>, norms: &BTreeMap<String, f64>) {

        let mut scores: FnvHashMap<String, f64> = FnvHashMap::default();

        for (term, weight) in &self.tokens[movie] {
            if !idfs.contains_key(term) { continue }
            let idf = idfs[term];
            let posting = &self.index[term];

            for (doc, tf) in posting {
                let score = scores.entry(doc.clone()).or_insert(0.0);
                *score += weight * tf * idf;
            }
        }
        
        for (doc, score) in &mut scores {
            *score /= norms[doc] * norms[movie];
        }

        let mut out = File::create(&format!("cosine/{}.json", movie)).unwrap();
        out.write_all(to_string(&scores).unwrap().as_bytes()).unwrap();
    }
}
