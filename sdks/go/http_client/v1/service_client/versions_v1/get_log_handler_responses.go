// Copyright 2019 Polyaxon, Inc.
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

package versions_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"

	strfmt "github.com/go-openapi/strfmt"

	service_model "github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// GetLogHandlerReader is a Reader for the GetLogHandler structure.
type GetLogHandlerReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *GetLogHandlerReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewGetLogHandlerOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewGetLogHandlerForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewGetLogHandlerNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("unknown error", response, response.Code())
	}
}

// NewGetLogHandlerOK creates a GetLogHandlerOK with default headers values
func NewGetLogHandlerOK() *GetLogHandlerOK {
	return &GetLogHandlerOK{}
}

/*GetLogHandlerOK handles this case with default header values.

A successful response.
*/
type GetLogHandlerOK struct {
	Payload *service_model.V1LogHandler
}

func (o *GetLogHandlerOK) Error() string {
	return fmt.Sprintf("[GET /api/v1/log_handler][%d] getLogHandlerOK  %+v", 200, o.Payload)
}

func (o *GetLogHandlerOK) GetPayload() *service_model.V1LogHandler {
	return o.Payload
}

func (o *GetLogHandlerOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.V1LogHandler)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewGetLogHandlerForbidden creates a GetLogHandlerForbidden with default headers values
func NewGetLogHandlerForbidden() *GetLogHandlerForbidden {
	return &GetLogHandlerForbidden{}
}

/*GetLogHandlerForbidden handles this case with default header values.

You don't have permission to access the resource.
*/
type GetLogHandlerForbidden struct {
	Payload interface{}
}

func (o *GetLogHandlerForbidden) Error() string {
	return fmt.Sprintf("[GET /api/v1/log_handler][%d] getLogHandlerForbidden  %+v", 403, o.Payload)
}

func (o *GetLogHandlerForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *GetLogHandlerForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewGetLogHandlerNotFound creates a GetLogHandlerNotFound with default headers values
func NewGetLogHandlerNotFound() *GetLogHandlerNotFound {
	return &GetLogHandlerNotFound{}
}

/*GetLogHandlerNotFound handles this case with default header values.

Resource does not exist.
*/
type GetLogHandlerNotFound struct {
	Payload string
}

func (o *GetLogHandlerNotFound) Error() string {
	return fmt.Sprintf("[GET /api/v1/log_handler][%d] getLogHandlerNotFound  %+v", 404, o.Payload)
}

func (o *GetLogHandlerNotFound) GetPayload() string {
	return o.Payload
}

func (o *GetLogHandlerNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}
