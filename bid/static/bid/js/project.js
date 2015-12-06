$(document).ready(function(){
    $(".login-box").width(550).height(500);
	$(".email-signup").hide();
	
$("#signup-box-link").click(function(){
 $(".login-box").width(550).height(550);
  //$(".email-login").fadIn(100);
  $(".email-signup").show();
  $(".email-login").hide();
  if($("input:radio[name=UserType]:checked").val()=='User'){
	  $('.userSinup').show();
	  $('.tarnsportSinup').hide();
	  }
	  else{
	 $('.userSinup').hide();
	  $('.tarnsportSinup').show();
		  
		  }
//$(".email-signup").delay(100).fadeIn(100);
  $("#login-box-link").removeClass("active");
  $("#signup-box-link").addClass("active");
});
$('input:radio[name=UserType]').change(function(){
$(".email-login").hide();
$(".email-signup").show();

 if($("input:radio[name=UserType]:checked").val()=='User'){
	  $('.userSinup').show();
	  $('.tarnsportSinup').hide();
	  }
	  else{
	 $('.userSinup').hide();
	  $('.tarnsportSinup').show();
		  
		  }


});


$("#login-box-link").click(function(){
$(".login-box").width(550).height(500);
$(".email-signup").hide();
  $(".email-login").show();
  //$(".email-login").delay(100).fadeIn(100);;
  //$(".email-signup").fadeOut(100);
  $("#login-box-link").addClass("active");
  $("#signup-box-link").removeClass("active");
});
$("#closing_date_picker").datepicker({dateFormat:'dd/mm/yy'}).val();
$("#closing_time_picker").timepicker();

});