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

package project_service

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
)

// NewListProjectNamesParams creates a new ListProjectNamesParams object
// with the default values initialized.
func NewListProjectNamesParams() *ListProjectNamesParams {
	var ()
	return &ListProjectNamesParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewListProjectNamesParamsWithTimeout creates a new ListProjectNamesParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewListProjectNamesParamsWithTimeout(timeout time.Duration) *ListProjectNamesParams {
	var ()
	return &ListProjectNamesParams{

		timeout: timeout,
	}
}

// NewListProjectNamesParamsWithContext creates a new ListProjectNamesParams object
// with the default values initialized, and the ability to set a context for a request
func NewListProjectNamesParamsWithContext(ctx context.Context) *ListProjectNamesParams {
	var ()
	return &ListProjectNamesParams{

		Context: ctx,
	}
}

// NewListProjectNamesParamsWithHTTPClient creates a new ListProjectNamesParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewListProjectNamesParamsWithHTTPClient(client *http.Client) *ListProjectNamesParams {
	var ()
	return &ListProjectNamesParams{
		HTTPClient: client,
	}
}

/*ListProjectNamesParams contains all the parameters to send to the API endpoint
for the list project names operation typically these are written to a http.Request
*/
type ListProjectNamesParams struct {

	/*Owner
	  Owner of the namespace

	*/
	Owner string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the list project names params
func (o *ListProjectNamesParams) WithTimeout(timeout time.Duration) *ListProjectNamesParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the list project names params
func (o *ListProjectNamesParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the list project names params
func (o *ListProjectNamesParams) WithContext(ctx context.Context) *ListProjectNamesParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the list project names params
func (o *ListProjectNamesParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the list project names params
func (o *ListProjectNamesParams) WithHTTPClient(client *http.Client) *ListProjectNamesParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the list project names params
func (o *ListProjectNamesParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithOwner adds the owner to the list project names params
func (o *ListProjectNamesParams) WithOwner(owner string) *ListProjectNamesParams {
	o.SetOwner(owner)
	return o
}

// SetOwner adds the owner to the list project names params
func (o *ListProjectNamesParams) SetOwner(owner string) {
	o.Owner = owner
}

// WriteToRequest writes these params to a swagger request
func (o *ListProjectNamesParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param owner
	if err := r.SetPathParam("owner", o.Owner); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
