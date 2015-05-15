angular.module('threeJsBlobApp').factory 'renderService', () ->
    class RenderService
        @renderer = new THREE.WebGLRenderer()
        @renderer.gammaInput = true
        @renderer.gammaOutput = true
        window.addEventListener('resize', @resize, false)
        @scene = new THREE.Scene()
        @camera = null
        @elem = null

        @resize = () =>
            if @elem?
                width = $(@elem).parent().width() - 10
                height = $(@elem).parent().height() - 10

                if !@camera?
                    @camera = new THREE.PerspectiveCamera(50, width / height, 1, 2000)
                    @camera.position.set(0, 0, 5)

                @renderer.setSize(width, height)
                @camera.aspect = width / height
                @camera.updateProjectionMatrix()

        @render_blob = (blob) =>
            current_blob = @scene.getObjectByName('blob')
            if current_blob?
                @scene.remove(current_blob)

            vertices = new Float32Array(blob)
            geometry = new THREE.BufferGeometry()
            geometry.addAttribute('position', new THREE.BufferAttribute(vertices, 3))
            geometry.computeBoundingSphere()
            material = new THREE.LineBasicMaterial({ color: 0xFF0000})
            lines = new THREE.Line(geometry, material, THREE.LinePieces)
            lines.name = 'blob'
            @scene.add(lines)

        @set_parent_elem = (elem) =>
            @elem = elem
            @resize()

        @render = () =>
            @renderer.render(@scene, @camera)

        @animate = () =>
            requestAnimationFrame(@animate)
            @render()