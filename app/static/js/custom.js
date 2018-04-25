$(document).ready(function() {
  $("#myCarousel").carousel({interval: false, wrap: false});

  $(".modal").map(function () {
    $(this).detach().appendTo($('body'));
  })

  $(".poster").click(function(){
    var id = this.getAttribute("data-movie");
    // var row = $(this).parent().parent();
    var mod = $('body').find("#"+id);

    // mod.detach().appendTo($('body'));

    mod.fadeIn(425);
  });

  $(".post_title").click(function(){
    var id = this.getAttribute("data-movie");
    // var row = $(this).parent().parent();
    var mod = $('body').find("#"+id);

    // mod.detach().appendTo($('body'));

    mod.fadeIn(425);
  });

  window.onclick = function(event) {
    if (event.target.className == "modal") {
        $(event.target).fadeOut(400);
    }
  }

  $(".advanced_button").click(function () {
    var search = $(this).parent().find(".advanced");
    search.slideToggle(400);
  });

  $("#slide1").click(function () { console.log('hello');});

  $("#slide2").click(function () { console.log('hello??');});

  // Action listeners for modal menu bar
  $("a[href='#overview']").click(function () {
    // Change menu bar css
    $(".current").removeClass("current");
    $(this).addClass("current");
    // Display content
    $("#overview_details").css("display","inline-block");
    $("#show_details").css("display","none");
  });

  $("a[href='#show']").click(function () {
    // Change css for menu bar
    $(".current").removeClass("current");
    $(this).addClass("current");
    // Display content
    $("#show_details").css("display","inline-block");
    $("#overview_details").css("display","none");
  });

  $("a[href='#search']").click(function () {
    $(".current").removeClass("current");
    $(this).addClass("current");
  });
});
