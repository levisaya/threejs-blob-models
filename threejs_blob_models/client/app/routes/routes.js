// Generated by CoffeeScript 1.8.0
(function() {
  angular.module('threeJsBlobApp').config(function($stateProvider, $urlRouterProvider) {
    var base_state, model_state;
    $urlRouterProvider.otherwise('/');
    base_state = {
      url: '/',
      name: 'base',
      views: {
        '@': {
          templateUrl: '/layout.html'
        },
        'sidebar@base': {
          controller: function($scope, model_types_response) {
            return $scope.model_types = model_types_response.data.model_types;
          },
          template: '<div ng-repeat="model_type in model_types"><a ui-sref="base.model({model_name:model_type})">{{model_type}}</a></div>',
          resolve: {
            'model_types_response': function($http) {
              return $http.get('/model-types');
            }
          }
        },
        'main_pane@base': {
          template: '<div>Pick One!</div>'
        }
      }
    };
    model_state = {
      url: 'model-display/:model_name',
      name: 'base.model',
      parent: base_state,
      views: {
        'main_pane@base': {
          template: '<renderer></renderer>',
          controller: function($scope, blob_response, renderService) {
            return renderService.render_blob(blob_response.data);
          },
          resolve: {
            'blob_response': function($http, $stateParams) {
              return $http.get('/model/' + $stateParams.model_name, {
                responseType: "arraybuffer"
              });
            }
          }
        }
      }
    };
    $stateProvider.state(base_state).state(model_state);
  });

}).call(this);