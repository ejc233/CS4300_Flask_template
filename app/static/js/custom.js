$(document).ready(function() {
  $("#myCarousel").carousel({interval: false, wrap: false});

  $(".modal").map(function () {
    $(this).detach().appendTo($('body'));
  })

  $(".poster").click(function(){
    var id = this.getAttribute("data-movie");
    var mod = $('body').find("#"+id);
    mod.fadeIn(425);
  });

  $(".post_title").click(function(){
    var id = this.getAttribute("data-movie");
    var mod = $('body').find("#"+id);
    mod.fadeIn(425);
  });

  window.onclick = function(event) {
    if (event.target.className == "modal") {
        $(event.target).fadeOut(400);
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
    $(".active_modal").hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    $(".overview_details").addClass("active_modal");
    $(".overview_details").show(300);
  });

  $("a[href='#show']").click(function () {
    // Remove old content
    $(".current").removeClass("current");
    $(".active_modal").hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    $(".show_details").addClass("active_modal");
    $(".show_details").show(300);
  });

  $("a[href='#search']").click(function () {
    // Remove old content
    $(".current").removeClass("current");
    $(".active_modal").hide(300);
    $(".active_modal").removeClass("active_modal");
    // Display new content
    $(this).addClass("current");
    // $().addClass("active"); //for later
    // $(".overview_details").css("display","inline-block");
  });
});
