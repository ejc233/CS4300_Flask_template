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
        //Remove whatever settings you left off on
        $(".current").removeClass("current");
        $(".active").css("display","none");
        $(".active").removeClass("active");
        //Reset back to original
        $("a[href='#overview']").addClass("current");
        $("a[href='#overview']").addClass("active");
        $("#overview_details").css("display","inline-block");
    }
  }

  $(".advanced_button").click(function () {
    var search = $(this).parent().find(".advanced");
    search.slideToggle(400);
  });

  // Action listeners for modal menu bar
  $("a[href='#overview']").click(function () {
    // Change menu bar css
    $(".current").removeClass("current");
    $(".active").css("display","none");
    $(".active").removeClass("active");
    $(this).addClass("current");
    $(this).addClass("active");
    // Display content
    $(".overview_details").show("slide", { direction: "right"  }, 500);
    $(".show_details").hide("slide", { direction: "right"  }, 500 );
  });

  $("a[href='#show']").click(function () {
    console.log("hello");
    // Change css for menu bar
    $(".current").removeClass("current");
    $(this).addClass("current");
    // Display content
    $(".show_details").show("slide", { direction: "left"  }, 500);
    $(".overview_details").hide("slide", { direction: "left"  }, 500 );
    console.log("goodbye");
  });

  $("a[href='#search']").click(function () {
    $(".current").removeClass("current");
    $(this).addClass("current");
  });
});
