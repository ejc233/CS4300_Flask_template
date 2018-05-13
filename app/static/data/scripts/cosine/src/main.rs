#[macro_use]
extern crate serde_derive;
extern crate serde;
extern crate serde_json;
extern crate cosine;

use cosine::index::Index;
use std::fs::File;
use std::io::Read;

#[derive(Deserialize)]
pub struct Cast {
    pub character: String,
    pub name: String,  
}

#[derive(Deserialize)]
pub struct Crew {
    pub job: String,
    pub name: String,
}

#[derive(Deserialize)]
pub struct Movie {
    pub id: String,
    pub cast: Vec<Cast>,
    pub crew: Vec<Crew>,
    pub title: String,
    pub genres: Vec<String>,
    pub keywords: Vec<String>,
    pub original_language: String,
    pub rating: String,
    pub release_date: String,
    pub revenue: f32,
    pub runtime: i32, 
    pub summary: String,
    pub tokens: Vec<String>,
    pub tmdb_score_value: f32,
    pub tmdb_score_count: i32,
    pub imdb_score_value: f32,
    pub imdb_score_count: i32,
    pub meta_score_value: f32,
    pub meta_score_count: i32,
}

#[derive(Deserialize, Debug)]
pub struct MovieIndex {
    pub id: String,
    pub title: String,
}

macro_rules! movie {
    ($id:expr) => (&format!("movies/{}.json", $id))
}

fn read(file: &str) -> String {
    let mut file = File::open(file).unwrap();
    let mut buffer = String::new();
    file.read_to_string(&mut buffer).unwrap();
    buffer
}

fn main() {

    let movies: Vec<MovieIndex> = serde_json::from_str(&read("movies.json")).unwrap();
    let mut index = Index::new();

    for movie in movies {
        let movie: Movie = serde_json::from_str(&read(movie!(movie.id))).unwrap();
        index.insert(movie.id, movie.title, movie.tokens);
    }

    index.process();
}
