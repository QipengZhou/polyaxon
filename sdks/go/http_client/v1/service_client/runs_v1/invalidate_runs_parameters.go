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

package runs_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"

	service_model "github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// NewInvalidateRunsParams creates a new InvalidateRunsParams object
// with the default values initialized.
func NewInvalidateRunsParams() *InvalidateRunsParams {
	var ()
	return &InvalidateRunsParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewInvalidateRunsParamsWithTimeout creates a new InvalidateRunsParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewInvalidateRunsParamsWithTimeout(timeout time.Duration) *InvalidateRunsParams {
	var ()
	return &InvalidateRunsParams{

		timeout: timeout,
	}
}

// NewInvalidateRunsParamsWithContext creates a new InvalidateRunsParams object
// with the default values initialized, and the ability to set a context for a request
func NewInvalidateRunsParamsWithContext(ctx context.Context) *InvalidateRunsParams {
	var ()
	return &InvalidateRunsParams{

		Context: ctx,
	}
}

// NewInvalidateRunsParamsWithHTTPClient creates a new InvalidateRunsParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewInvalidateRunsParamsWithHTTPClient(client *http.Client) *InvalidateRunsParams {
	var ()
	return &InvalidateRunsParams{
		HTTPClient: client,
	}
}

/*InvalidateRunsParams contains all the parameters to send to the API endpoint
for the invalidate runs operation typically these are written to a http.Request
*/
type InvalidateRunsParams struct {

	/*Body
	  Uuids of the entities

	*/
	Body *service_model.V1Uuids
	/*Owner
	  Owner of the namespace

	*/
	Owner string
	/*Project
	  Project under namesapce

	*/
	Project string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the invalidate runs params
func (o *InvalidateRunsParams) WithTimeout(timeout time.Duration) *InvalidateRunsParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the invalidate runs params
func (o *InvalidateRunsParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the invalidate runs params
func (o *InvalidateRunsParams) WithContext(ctx context.Context) *InvalidateRunsParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the invalidate runs params
func (o *InvalidateRunsParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the invalidate runs params
func (o *InvalidateRunsParams) WithHTTPClient(client *http.Client) *InvalidateRunsParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the invalidate runs params
func (o *InvalidateRunsParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithBody adds the body to the invalidate runs params
func (o *InvalidateRunsParams) WithBody(body *service_model.V1Uuids) *InvalidateRunsParams {
	o.SetBody(body)
	return o
}

// SetBody adds the body to the invalidate runs params
func (o *InvalidateRunsParams) SetBody(body *service_model.V1Uuids) {
	o.Body = body
}

// WithOwner adds the owner to the invalidate runs params
func (o *InvalidateRunsParams) WithOwner(owner string) *InvalidateRunsParams {
	o.SetOwner(owner)
	return o
}

// SetOwner adds the owner to the invalidate runs params
func (o *InvalidateRunsParams) SetOwner(owner string) {
	o.Owner = owner
}

// WithProject adds the project to the invalidate runs params
func (o *InvalidateRunsParams) WithProject(project string) *InvalidateRunsParams {
	o.SetProject(project)
	return o
}

// SetProject adds the project to the invalidate runs params
func (o *InvalidateRunsParams) SetProject(project string) {
	o.Project = project
}

// WriteToRequest writes these params to a swagger request
func (o *InvalidateRunsParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.Body != nil {
		if err := r.SetBodyParam(o.Body); err != nil {
			return err
		}
	}

	// path param owner
	if err := r.SetPathParam("owner", o.Owner); err != nil {
		return err
	}

	// path param project
	if err := r.SetPathParam("project", o.Project); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
