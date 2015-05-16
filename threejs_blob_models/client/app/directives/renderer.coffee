# Directive to place the three.js renderer from the rendererService in the current view, and start the render loop.

angular.module('threeJsBlobApp').directive 'renderer', (renderService) ->
    restrict: 'E',
    link: (scope, elem, attrs) ->
        # Set the parent element in the renderer service so we can resize the renderer on window resize.
        renderer_elem = renderService.set_parent_elem($(elem[0]).parent())

        # Add the renderer dom element under the renderer directive element.
        elem.append(renderer_elem)

        # Start the renderer loop.
        renderService.start_render()

        # Set up a handler to stop rendering when the renderer directive is destroyed.
        # No need to be rendering when we can't see it.
        scope.$on '$destroy', () ->
            renderService.cancel_render()
