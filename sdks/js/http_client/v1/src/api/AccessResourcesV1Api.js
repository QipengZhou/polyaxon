// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * OpenAPI spec version: 1.0.71
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.10
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/RuntimeError', 'model/V1AccessResource', 'model/V1ListAccessResourcesResponse'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/RuntimeError'), require('../model/V1AccessResource'), require('../model/V1ListAccessResourcesResponse'));
  } else {
    // Browser globals (root is window)
    if (!root.PolyaxonSdk) {
      root.PolyaxonSdk = {};
    }
    root.PolyaxonSdk.AccessResourcesV1Api = factory(root.PolyaxonSdk.ApiClient, root.PolyaxonSdk.RuntimeError, root.PolyaxonSdk.V1AccessResource, root.PolyaxonSdk.V1ListAccessResourcesResponse);
  }
}(this, function(ApiClient, RuntimeError, V1AccessResource, V1ListAccessResourcesResponse) {
  'use strict';

  /**
   * AccessResourcesV1 service.
   * @module api/AccessResourcesV1Api
   * @version 1.0.71
   */

  /**
   * Constructs a new AccessResourcesV1Api. 
   * @alias module:api/AccessResourcesV1Api
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the createAccessResource operation.
     * @callback module:api/AccessResourcesV1Api~createAccessResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1AccessResource} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create access resource
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1AccessResource} body Artifact store body
     * @param {module:api/AccessResourcesV1Api~createAccessResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1AccessResource}
     */
    this.createAccessResource = function(owner, body, callback) {
      var postBody = body;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling createAccessResource");
      }

      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling createAccessResource");
      }


      var pathParams = {
        'owner': owner
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1AccessResource;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteAccessResource operation.
     * @callback module:api/AccessResourcesV1Api~deleteAccessResourceCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete access resource
     * @param {String} owner Owner of the namespace
     * @param {String} uuid Uuid identifier of the entity
     * @param {module:api/AccessResourcesV1Api~deleteAccessResourceCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.deleteAccessResource = function(owner, uuid, callback) {
      var postBody = null;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling deleteAccessResource");
      }

      // verify the required parameter 'uuid' is set
      if (uuid === undefined || uuid === null) {
        throw new Error("Missing the required parameter 'uuid' when calling deleteAccessResource");
      }


      var pathParams = {
        'owner': owner,
        'uuid': uuid
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = null;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources/{uuid}', 'DELETE',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccessResource operation.
     * @callback module:api/AccessResourcesV1Api~getAccessResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1AccessResource} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get access resource
     * @param {String} owner Owner of the namespace
     * @param {String} uuid Uuid identifier of the entity
     * @param {module:api/AccessResourcesV1Api~getAccessResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1AccessResource}
     */
    this.getAccessResource = function(owner, uuid, callback) {
      var postBody = null;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getAccessResource");
      }

      // verify the required parameter 'uuid' is set
      if (uuid === undefined || uuid === null) {
        throw new Error("Missing the required parameter 'uuid' when calling getAccessResource");
      }


      var pathParams = {
        'owner': owner,
        'uuid': uuid
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1AccessResource;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources/{uuid}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the listAccessResourceNames operation.
     * @callback module:api/AccessResourcesV1Api~listAccessResourceNamesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListAccessResourcesResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List access resource names
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {Number} opts.offset Pagination offset.
     * @param {Number} opts.limit Limit size.
     * @param {String} opts.sort Sort to order the search.
     * @param {String} opts.query Query filter the search search.
     * @param {module:api/AccessResourcesV1Api~listAccessResourceNamesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListAccessResourcesResponse}
     */
    this.listAccessResourceNames = function(owner, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling listAccessResourceNames");
      }


      var pathParams = {
        'owner': owner
      };
      var queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort'],
        'query': opts['query'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1ListAccessResourcesResponse;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources/names', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the listAccessResources operation.
     * @callback module:api/AccessResourcesV1Api~listAccessResourcesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListAccessResourcesResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List access resources
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {Number} opts.offset Pagination offset.
     * @param {Number} opts.limit Limit size.
     * @param {String} opts.sort Sort to order the search.
     * @param {String} opts.query Query filter the search search.
     * @param {module:api/AccessResourcesV1Api~listAccessResourcesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListAccessResourcesResponse}
     */
    this.listAccessResources = function(owner, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling listAccessResources");
      }


      var pathParams = {
        'owner': owner
      };
      var queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort'],
        'query': opts['query'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1ListAccessResourcesResponse;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the patchAccessResource operation.
     * @callback module:api/AccessResourcesV1Api~patchAccessResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1AccessResource} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch access resource
     * @param {String} owner Owner of the namespace
     * @param {String} access_resource_uuid UUID
     * @param {module:model/V1AccessResource} body Artifact store body
     * @param {module:api/AccessResourcesV1Api~patchAccessResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1AccessResource}
     */
    this.patchAccessResource = function(owner, access_resource_uuid, body, callback) {
      var postBody = body;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchAccessResource");
      }

      // verify the required parameter 'access_resource_uuid' is set
      if (access_resource_uuid === undefined || access_resource_uuid === null) {
        throw new Error("Missing the required parameter 'access_resource_uuid' when calling patchAccessResource");
      }

      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchAccessResource");
      }


      var pathParams = {
        'owner': owner,
        'access_resource.uuid': access_resource_uuid
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1AccessResource;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources/{access_resource.uuid}', 'PATCH',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the updateAccessResource operation.
     * @callback module:api/AccessResourcesV1Api~updateAccessResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1AccessResource} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update access resource
     * @param {String} owner Owner of the namespace
     * @param {String} access_resource_uuid UUID
     * @param {module:model/V1AccessResource} body Artifact store body
     * @param {module:api/AccessResourcesV1Api~updateAccessResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1AccessResource}
     */
    this.updateAccessResource = function(owner, access_resource_uuid, body, callback) {
      var postBody = body;

      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateAccessResource");
      }

      // verify the required parameter 'access_resource_uuid' is set
      if (access_resource_uuid === undefined || access_resource_uuid === null) {
        throw new Error("Missing the required parameter 'access_resource_uuid' when calling updateAccessResource");
      }

      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateAccessResource");
      }


      var pathParams = {
        'owner': owner,
        'access_resource.uuid': access_resource_uuid
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['ApiKey'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = V1AccessResource;

      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/access_resources/{access_resource.uuid}', 'PUT',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
