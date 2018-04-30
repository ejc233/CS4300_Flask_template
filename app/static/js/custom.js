$(document).ready(function() {
  var scores = ['similar', 'genres', 'cast',
  'keywords', 'duration', 'release', 'ratings',
  'languages', 'acclaim', 'popularity'];
  $("#myCarousel").carousel({interval: false, wrap: false});

  $(".modal").map(function () {
    $(this).detach().appendTo($('body'));
  })

  var chart;

  function addGraph(id, score_dict){
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

    var myBarChart = new Chart(chart_el, {
      type: 'bar',
      data: barChartData,
      options: {
        maintainAspectRatio: true,
        layout: {
          padding: {
                left: 10,
                right: 10,
                top: 0,
                bottom: 0
            }
        },
        legend: {
          display: false
        },
        responsive: false,
        title: {
          display: true,
          text: 'Similarity Score Breakdown',
          fontSize: 18,
          fontColor: "rgb(255,255,255)"
        },
        scales: {
          yAxes: [{
              ticks: {
                  fontColor: "white",
                  beginAtZero: true,
                  max: 1.0,
                  fontSize: 14
              },
              gridLines: {
                  display: false,
                  color: "white"
              }
          }],
          xAxes: [{
              ticks: {
                  fontColor: "white",
                  autoSkip: false,
                  fontSize: 14
              },
              gridLines: {
                  display: false,
                  color: "white"
              }
          }]
        },
      }
    });
  }

  function popupModal(poster){
    var id = poster.getAttribute("data-movie");
    var scores = (poster.getAttribute("data-scores")).replace(/'/g, '"');
    var mod = $('body').find("#"+id);
    var e = $("<canvas></canvas>")
    var chart_div = mod.find(".search_details").append(e);
    e.attr('id', id+"_chart");
    addGraph(id+"_chart", JSON.parse(scores));
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
        var canv = $(event.target).find("canvas");
        canv.remove();
        $(".contents").removeClass("blur_overlay");
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
