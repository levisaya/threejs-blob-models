angular.module('threeJsBlobApp').config ($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider.otherwise('/')

    base_state =
        url: '/'
        name: 'base'
        views:
            '@':
                templateUrl: '/layout.html'
            'sidebar@base':
                controller: ($scope, model_types_response) ->
                    $scope.model_types = model_types_response.data.model_types
                template: '<div ng-repeat="model_type in model_types"><a ui-sref="base.model({model_name:model_type})">{{model_type}}</a></div>'
                resolve:
                    'model_types_response': ($http) -> $http.get('/model-types')
            'main_pane@base':
                template: '<div>Pick One!</div>'

    model_state =
        url: 'model-display/:model_name'
        name: 'base.model'
        parent: base_state
        views:
            'main_pane@base':
                template: '<renderer></renderer>'
                controller: ($scope, blob_response, renderService) ->
                    renderService.render_blob(blob_response.data)
                resolve:
                    'blob_response': ($http, $stateParams) -> $http.get('/model/' + $stateParams.model_name, {responseType: "arraybuffer"})

    $stateProvider.state(base_state).state(model_state)
    return