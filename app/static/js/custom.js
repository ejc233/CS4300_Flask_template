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

    mod.show("medium");
    // console.log(mod);
  });

  $(".post_title").click(function(){
    var id = this.getAttribute("data-movie");
    // var row = $(this).parent().parent();
    var mod = $('body').find("#"+id);

    // mod.detach().appendTo($('body'));

    mod.show(400);
    // console.log(mod);
  });

  window.onclick = function(event) {
    console.log(event.target);
    if (event.target.className == "modal") {
        $(event.target).hide(400);
    }
  }

  $(".advanced_button").click(function () {
    var search = $(this).parent().find(".advanced");
    search.slideToggle(400);
  })
});
