$(document).ready(function() {
  var scores = ['similar movies', 'genres', 'cast',
  'keywords', 'duration', 'release', 'ratings',
  'languages', 'acclaim', 'popularity'];
  $("#myCarousel").carousel({interval: false, wrap: false});

  $(".modal").map(function () {
    $(this).detach().appendTo($('body'));
  });

  var myBarChart;

  function addGraph(id, score_dict, elt){
    var chart_el = document.getElementById(id).getContext('2d');
    scores_list = [];
    scores.forEach(function(d){
      if(score_dict.hasOwnProperty(d)){
        scores_list.push(score_dict[d]);
      }
      else{
        scores_list.push(0);
      }
    });

    var barChartData = {
      labels: scores,
      datasets: [{
        backgroundColor: 'rgb(117, 147, 206)',
        borderColor: 'rgb(135, 160, 209)',
        borderWidth: 1,
        data: scores_list
      }]};

    myBarChart = new Chart(chart_el, {
      type: 'bar',
      data: barChartData,
      options: {
        devicePixelRatio: 3,
        maintainAspectRatio: true,
        layout: {
          padding: {
                left: 10,
                right: 10,
                top: 3,
                bottom: 3
            }
        },
        legend: {
          display: false
        },
        responsive: false,
        title: {
          display: true,
          text: 'Similarity Score Breakdown',
          fontSize: 22,
          fontColor: "rgb(255,255,255)",
          padding: 10,
          fontFamily: "'Play', sans-serif"
        },
        scales: {
          yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Match (%)',
                fontColor: "white",
                fontSize: 16,
                fontFamily: "'Play', sans-serif",
                padding: {
                  top: 5
                }
              },
              ticks: {
                  fontColor: "white",
                  beginAtZero: true,
                  fontFamily: "'Play', sans-serif",
                  max: 100,
                  fontSize: 14
              },
              gridLines: {
                  display: false,
                  color: "white"
              }
          }],
          xAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Input Type',
                fontColor: "white",
                fontSize: 16,
                fontFamily: "'Play', sans-serif",
                lineHeight: 3.0,
                padding: {
                  top: 0
                }
              },
              ticks: {
                  fontColor: "white",
                  autoSkip: false,
                  fontSize: 14,
                  fontFamily: "'Play', sans-serif"
              },
              gridLines: {
                  display: false,
                  color: "white"
              }
          }]
        },
      }
    });

    var text = "<div id='canvas_details' class='canvas_details'><strong class='heading2'>Your search inputs: </strong><br>"
                + score_dict["old_inputs"]
                + "<br><strong class='heading2'>Movie's similarity score to your search: </strong><br>"
                + score_dict["overall_score"] + "%</div>";
    var text2 = "<div id='canvas_details2' class='canvas_details' style='float: right'><strong class='heading2'>Plot explanation:<br></strong>"
                + "This bar graph visualizes how well each attribute of this recommended movie matches each input attribute in your search."
                + " The acclaim and popularity scores represent what percentile the movie is in for that category."
                + " Hover over each bar to see how well this movie matches your inputs!</div>";

    //Add the text
    var mod = $('body').find("#"+elt).find(".search_details").append(text);
    var mod = $('body').find("#"+elt).find(".search_details").append(text2);
  }

  function popupModal(poster){
    var id = poster.getAttribute("data-movie");
    var scores = (poster.getAttribute("data-scores")).replace(/'/g, '"');
    var mod = $('body').find("#"+id);
    var e = $("<canvas></canvas>");
    var chart_div = mod.find(".search_details").append(e);
    e.attr('id', id+"_chart");
    addGraph(id+"_chart", JSON.parse(scores), id);
    mod.fadeIn(425);
    $(".contents").addClass("blur_overlay");
  }

  $(".poster").click(function(){
    popupModal(this);
  });

  $(".post_title").click(function(){
    popupModal(this);
  });

  window.onclick = function(event) {
    if (event.target.className == "modal") {
        $(event.target).fadeOut(400);
        myBarChart.destroy();
        var canv = $(event.target).find("canvas");
        canv.remove();
        $(".contents").removeClass("blur_overlay");
        $(event.target).find("#canvas_details").remove();
        $(event.target).find("#canvas_details2").remove();
        //Remove whatever settings you left off on
        $(".current").removeClass("current");
        $(".active_modal").css("display","none");
        $(".active_modal").removeClass("active_modal");
        //Reset back to original
        $("a[href='#overview']").addClass("current");
        $(".overview_details").addClass("active_modal");
        $(".overview_details").css("display","inline-block");
    }
  }

  $(".advanced_button").click(function () {
    var search = $(this).parent().find(".advanced");
    search.slideToggle(400);
  });

  // Action listeners for modal menu bar
  $("a[href='#overview']").click(function () {
    // Remove old content
    $(".current").removeClass("current");
    $(".active_modal").stop().hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    $(".overview_details").addClass("active_modal");
    $(".overview_details").stop().show(300);
  });

  $("a[href='#show']").click(function () {
    // Remove old content
    $(".current").removeClass("current");
    $(".active_modal").stop().hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    $(".show_details").addClass("active_modal");
    $(".show_details").stop().show(300);
  });

  $("a[href='#search']").click(function () {
    // Remove old content
    $(".current").removeClass("current");
    $(".active_modal").stop().hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    $(".search_details").addClass("active_modal");
    $(".search_details").stop().show(300);
  });
});
