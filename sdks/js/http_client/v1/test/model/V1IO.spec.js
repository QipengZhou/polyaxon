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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PolyaxonSdk);
  }
}(this, function(expect, PolyaxonSdk) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('V1IO', function() {
      beforeEach(function() {
        instance = new PolyaxonSdk.V1IO();
      });

      it('should create an instance of V1IO', function() {
        // TODO: update the code to test V1IO
        expect(instance).to.be.a(PolyaxonSdk.V1IO);
      });

      it('should have the property name (base name: "name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property description (base name: "description")', function() {
        // TODO: update the code to test the property description
        expect(instance).to.have.property('description');
        // expect(instance.description).to.be(expectedValueLiteral);
      });

      it('should have the property iotype (base name: "iotype")', function() {
        // TODO: update the code to test the property iotype
        expect(instance).to.have.property('iotype');
        // expect(instance.iotype).to.be(expectedValueLiteral);
      });

      it('should have the property value (base name: "value")', function() {
        // TODO: update the code to test the property value
        expect(instance).to.have.property('value');
        // expect(instance.value).to.be(expectedValueLiteral);
      });

      it('should have the property is_optional (base name: "is_optional")', function() {
        // TODO: update the code to test the property is_optional
        expect(instance).to.have.property('is_optional');
        // expect(instance.is_optional).to.be(expectedValueLiteral);
      });

      it('should have the property is_list (base name: "is_list")', function() {
        // TODO: update the code to test the property is_list
        expect(instance).to.have.property('is_list');
        // expect(instance.is_list).to.be(expectedValueLiteral);
      });

      it('should have the property is_flag (base name: "is_flag")', function() {
        // TODO: update the code to test the property is_flag
        expect(instance).to.have.property('is_flag');
        // expect(instance.is_flag).to.be(expectedValueLiteral);
      });

      it('should have the property delay_validation (base name: "delay_validation")', function() {
        // TODO: update the code to test the property delay_validation
        expect(instance).to.have.property('delay_validation');
        // expect(instance.delay_validation).to.be(expectedValueLiteral);
      });

      it('should have the property options (base name: "options")', function() {
        // TODO: update the code to test the property options
        expect(instance).to.have.property('options');
        // expect(instance.options).to.be(expectedValueLiteral);
      });

    });
  });

}));
