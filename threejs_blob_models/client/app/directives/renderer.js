// Generated by CoffeeScript 1.8.0
(function() {
  angular.module('threeJsBlobApp').directive('renderer', function(renderService) {
    return {
      restrict: 'E',
      link: function(scope, elem, attrs) {
        renderService.set_parent_elem(elem[0]);
        elem.append(renderService.renderer.domElement);
        return renderService.animate();
      }
    };
  });

}).call(this);