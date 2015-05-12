angular.module('threeJsBlobApp').directive 'renderer', () ->
    restrict: 'E',
    link: (scope, elem, attrs) ->
        camera = null
        scene = null
        renderer = null

        on_resize = () ->
            width = $(elem).parent().width() - 10
            height = $(elem).parent().height() - 10
            renderer.setSize(width, height)
            camera.aspect = width / height
            camera.updateProjectionMatrix()

        init = () ->
            width = $(elem).parent().width() - 10
            height = $(elem).parent().height() - 10
            camera = new THREE.PerspectiveCamera(50, width / height, 1, 2000)
            camera.position.set(0, 0, 1)

            scene = new THREE.Scene()
            scene.add(new THREE.AmbientLight(0x000000));

            renderer = new THREE.WebGLRenderer();
            renderer.setSize(width, height);
            elem[0].appendChild(renderer.domElement);

            window.addEventListener('resize', on_resize, false);

           #vertices = new Float32Array(blob)
           #geometry = new THREE.BufferGeometry()
           #geometry.addAttribute('position', new THREE.BufferAttribute(vertices, 3))
           #material = new THREE.MeshBasicMaterial({ color: 0x000000})
           #mesh = new THREE.Mesh(geometry, material)
           #scene.add(mesh)

        render = () ->
            renderer.render(scene, camera)

        animate = () ->
            requestAnimationFrame(animate)
            render()

        init()
        animate()
