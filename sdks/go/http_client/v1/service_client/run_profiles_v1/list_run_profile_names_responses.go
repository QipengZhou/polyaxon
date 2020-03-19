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

// Code generated by go-swagger; DO NOT EDIT.

package run_profiles_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// ListRunProfileNamesReader is a Reader for the ListRunProfileNames structure.
type ListRunProfileNamesReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *ListRunProfileNamesReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewListRunProfileNamesOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 204:
		result := NewListRunProfileNamesNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewListRunProfileNamesForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewListRunProfileNamesNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	default:
		result := NewListRunProfileNamesDefault(response.Code())
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		if response.Code()/100 == 2 {
			return result, nil
		}
		return nil, result
	}
}

// NewListRunProfileNamesOK creates a ListRunProfileNamesOK with default headers values
func NewListRunProfileNamesOK() *ListRunProfileNamesOK {
	return &ListRunProfileNamesOK{}
}

/*ListRunProfileNamesOK handles this case with default header values.

A successful response.
*/
type ListRunProfileNamesOK struct {
	Payload *service_model.V1ListRunProfilesResponse
}

func (o *ListRunProfileNamesOK) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/run_profiles/names][%d] listRunProfileNamesOK  %+v", 200, o.Payload)
}

func (o *ListRunProfileNamesOK) GetPayload() *service_model.V1ListRunProfilesResponse {
	return o.Payload
}

func (o *ListRunProfileNamesOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.V1ListRunProfilesResponse)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListRunProfileNamesNoContent creates a ListRunProfileNamesNoContent with default headers values
func NewListRunProfileNamesNoContent() *ListRunProfileNamesNoContent {
	return &ListRunProfileNamesNoContent{}
}

/*ListRunProfileNamesNoContent handles this case with default header values.

No content.
*/
type ListRunProfileNamesNoContent struct {
	Payload interface{}
}

func (o *ListRunProfileNamesNoContent) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/run_profiles/names][%d] listRunProfileNamesNoContent  %+v", 204, o.Payload)
}

func (o *ListRunProfileNamesNoContent) GetPayload() interface{} {
	return o.Payload
}

func (o *ListRunProfileNamesNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListRunProfileNamesForbidden creates a ListRunProfileNamesForbidden with default headers values
func NewListRunProfileNamesForbidden() *ListRunProfileNamesForbidden {
	return &ListRunProfileNamesForbidden{}
}

/*ListRunProfileNamesForbidden handles this case with default header values.

You don't have permission to access the resource.
*/
type ListRunProfileNamesForbidden struct {
	Payload interface{}
}

func (o *ListRunProfileNamesForbidden) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/run_profiles/names][%d] listRunProfileNamesForbidden  %+v", 403, o.Payload)
}

func (o *ListRunProfileNamesForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *ListRunProfileNamesForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListRunProfileNamesNotFound creates a ListRunProfileNamesNotFound with default headers values
func NewListRunProfileNamesNotFound() *ListRunProfileNamesNotFound {
	return &ListRunProfileNamesNotFound{}
}

/*ListRunProfileNamesNotFound handles this case with default header values.

Resource does not exist.
*/
type ListRunProfileNamesNotFound struct {
	Payload interface{}
}

func (o *ListRunProfileNamesNotFound) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/run_profiles/names][%d] listRunProfileNamesNotFound  %+v", 404, o.Payload)
}

func (o *ListRunProfileNamesNotFound) GetPayload() interface{} {
	return o.Payload
}

func (o *ListRunProfileNamesNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListRunProfileNamesDefault creates a ListRunProfileNamesDefault with default headers values
func NewListRunProfileNamesDefault(code int) *ListRunProfileNamesDefault {
	return &ListRunProfileNamesDefault{
		_statusCode: code,
	}
}

/*ListRunProfileNamesDefault handles this case with default header values.

An unexpected error response
*/
type ListRunProfileNamesDefault struct {
	_statusCode int

	Payload *service_model.RuntimeError
}

// Code gets the status code for the list run profile names default response
func (o *ListRunProfileNamesDefault) Code() int {
	return o._statusCode
}

func (o *ListRunProfileNamesDefault) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/run_profiles/names][%d] ListRunProfileNames default  %+v", o._statusCode, o.Payload)
}

func (o *ListRunProfileNamesDefault) GetPayload() *service_model.RuntimeError {
	return o.Payload
}

func (o *ListRunProfileNamesDefault) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.RuntimeError)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}