	



$(document).ready(function(){
	
$('.voodoo_popup1, .voodoo_popup2, .voodoo_popup3').hide(); 
$(".voodoo_link1").mouseover(function(e){
	e.stopPropagation();
    $(".voodoo_popup1").show();
	$(".voodoo_link1").removeClass("active");
	$(".top_content_main p, .top_row_content").hide();
});
	
$(".voodoo_link1").mouseout(function(e){
	e.stopPropagation();
    $(".voodoo_popup1").hide();
	$(".voodoo_link1").addClass("active");
	$(".top_content_main p, .top_row_content").show();
});
    
$(".voodoo_link2").mouseover(function(e){
	e.stopPropagation();
    $(".voodoo_popup2").show();
	$(".voodoo_link2").removeClass("active");
	$(".top_content_main p, .top_row_content").hide();
});
	
$(".voodoo_link2").mouseout(function(e){
	e.stopPropagation();
    $(".voodoo_popup2").hide();
	$(".voodoo_link2").addClass("active");
	$(".top_content_main p, .top_row_content").show();
});
	
	
$(".voodoo_link3").mouseover(function(e){
	e.stopPropagation();
    $(".voodoo_popup3").show();
	$(".voodoo_link3").removeClass("active");
	$(".top_content_main p, .top_row_content").hide();
	});
		
});


