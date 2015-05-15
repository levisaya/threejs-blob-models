angular.module('threeJsBlobApp').directive 'renderer', (renderService) ->
    restrict: 'E',
    link: (scope, elem, attrs) ->
        renderService.set_parent_elem(elem[0])
        elem.append(renderService.renderer.domElement)
        renderService.animate()
