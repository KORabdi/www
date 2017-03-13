app.directive('youtube', function($window,revloPatch) {
  return {
    restrict: "E",

    scope: {
      height:   "@",
      width:    "@",
      videoid:  "@"  
    },

    template: '<div></div>',

    link: function(scope, element) {
      var tag = document.createElement('script');
      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      var player;

      $window.onYouTubeIframeAPIReady = function() {
        player = new YT.Player(element.children()[0], {
          height: scope.height,
          width: scope.width,
          videoId: scope.videoid,
          
          events: {
              'onReady': onPlayerReady,
              'onStateChange': onPlayerStateChange
          }
        });
      };
      function onPlayerReady(event) {
    	  //player.playVideo();
    	  var a = 'a';
      }
      
      function onPlayerStateChange(event) {        
    	    if(event.data === 0) {    
    	    	player.loadVideoById('GMDqA3DkAEw'); //include array from view/controler
    	    	revloPatch.content('1458481',true);
    	    }
    	}
    },  
  }
});