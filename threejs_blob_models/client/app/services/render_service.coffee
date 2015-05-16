# Service to hold onto all the three.js guts. This way, we don't have to reinitialize all of it when switching
# between views.

angular.module('threeJsBlobApp').factory 'renderService', () ->
    class RenderService
        # Initialize the renderer and scene for the lifetime of the app.
        # These don't depend on any of the DOM, so they can just stay constant.
        @renderer = new THREE.WebGLRenderer()
        @renderer.gammaInput = true
        @renderer.gammaOutput = true
        @scene = new THREE.Scene()

        # The camera needs to be initialized later when we know the dimensions of the parent DOM element.
        @camera = null

        # We hold onto a reference to the parent DOM element so we can change the renderer size on window resize.
        @elem = null

        # Set the new dimensions on the camera and renderer when either the window changes size, or when there is
        # a new parent DOM element.
        @resize = () =>
            if @elem?
                width = $(@elem).width() - 4
                height = $(@elem).height() - 4

                # The camera only needs to be initialized once, on setting the initial parent DOM element.
                if !@camera?
                    @camera = new THREE.PerspectiveCamera(50, width / height, 1, 2000)
                    @camera.position.set(0, 0, 5)

                # Resize the renderer and adjust the camera.
                @renderer.setSize(width, height)
                @camera.aspect = width / height
                @camera.updateProjectionMatrix()

        # Resize everything when the window is resized.
        window.addEventListener('resize', @resize, false)

        # Render a binary array of geometry data as a GL LinePieces.
        @render_blob = (blob) =>
            # If we already have an object in the scene that we previously added, remove it.
            current_blob = @scene.getObjectByName('blob')
            if current_blob?
                @scene.remove(current_blob)

            # Blob comes in as an ArrayBuffer. Turn it into a Float32Array, make it into geometry and add it to
            # the scene.
            vertices = new Float32Array(blob)
            geometry = new THREE.BufferGeometry()
            geometry.addAttribute('position', new THREE.BufferAttribute(vertices, 3))
            geometry.computeBoundingSphere()
            material = new THREE.LineBasicMaterial({ color: 0xFF0000})
            lines = new THREE.Line(geometry, material, THREE.LinePieces)
            lines.name = 'blob'
            @scene.add(lines)

        @set_parent_elem = (elem) =>
            # Set the parent DOM element so we can handle resizes.
            @elem = elem
            @resize()
            return @renderer.domElement

        # Keep track of the animation id so we can cancel the renderer loop.
        @animation_id = null

        @cancel_render = () =>
            # Break out of the render loop.
            if @animation_id
                cancelAnimationFrame(@animation_id)
            @animation_id = null

        @render = () =>
            time = Date.now() * 0.001;
            blob = @scene.getObjectByName('blob')
            blob.rotation.x = time * 0.25;
            blob.rotation.y = time * 0.5;
            @renderer.render(@scene, @camera)

        @start_render = () =>
            @animation_id = requestAnimationFrame(@start_render)
            @render()