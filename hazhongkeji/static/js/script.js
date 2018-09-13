$(document).ready(function(){   
  
    $("ul.subnav").parent().append("<span></span>"); //Only shows drop down trigger when js is enabled (Adds empty span tag after ul.subnav*)   
  
    $("ul.topnav li span").mouseover(function() { //When trigger is clicked...   
  
        //Following events are applied to the subnav itself (moving subnav up and down)   
        $(this).parent().find("ul.subnav").slideDown('fast').show(); //Drop down the subnav on click   
  
        $(this).parent().hover(function() {   
        }, function(){   
            $(this).parent().find("ul.subnav").slideUp('slow'); //When the mouse hovers out of the subnav, move it back up   
        });   
  
        //Following events are applied to the trigger (Hover events for the trigger)   
        }).hover(function() {   
            $(this).addClass("subhover"); //On hover over, add class "subhover"   
        }, function(){  //On Hover Out   
            $(this).removeClass("subhover"); //On hover out, remove class "subhover"   
    });   
    $(".subnav li").each(function(){
        var lh=$(".left").find('h3').html();
        if($(this).html().indexOf(lh)!=-1){
            $(this).remove();
        }

    });
    if (window.screen.width=='1280'){
        $("body").css({zoom:"95%"});
    }else if (window.screen.width=='1024')  {
        $("body").css({zoom:"80%"});
    }else if (window.screen.width<=768)  {
        $("body").css({zoom:"64%"});
        $("#foot1").css({height:280});
    }
});  
