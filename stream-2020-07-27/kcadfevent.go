package main
// This code won't run and was just an exercise

import (
	"github.com/gofrs/uuid"
)
// adapted from notque/gocadf
// Event contains the CADF event according to CADF spec, section 6.6.1 Event (data)
// Extensions: requestPath (OpenStack, IBM), initiator.project_id/domain_id
// Omissions: everything that we do not use or not expose to API users
//  The JSON annotations are for parsing the result from ElasticSearch AND for generating the Hermes API response
type Event struct {
	TypeURI     string       `json:"typeURI"`
	ID          string       `json:"id"`
	EventTime   string       `json:"eventTime"`
	Action      string       `json:"action"`
	EventType   string       `json:"eventType"`
	Outcome     string       `json:"outcome"`
	Reason      Reason       `json:"reason,omitempty"`
	Initiator   Resource     `json:"initiator"`
	Target      Resource     `json:"target"`
	Observer    Resource     `json:"observer"`
	Attachments []Attachment `json:"attachments,omitempty"`
	// requestPath is an extension of OpenStack's pycadf which is supported by IBM as well
	RequestPath string `json:"requestPath,omitempty"`
}



ev := Event{
	TypeURI:    "http://schemas.dmtf.org/cloud/audit/1.0/event",
	ID:         generateUUID(),
	EventTime   time.time(),
	Action      cadfAction,
	EventType   "activity" // there are only a few options and activity is pretty much it
	Outcome     cadfOutcome
	Reason      cadfReason
	Initiator   ka.user.name,
	Target      %ka.target.name/%ka.target.resource/%ka.target.namespace
	Observer    "k8saudit/falco/clustername" 
	Attachments 0,
	// requestPath is an extension of OpenStack's pycadf which is supported by IBM as well
	RequestPath ka.uri,
}

// Reason contains HTTP Code and Type, and is optional in the CADF spec
type Reason struct {
	ReasonCode string `json:"reasonCode,omitempty"`
	ReasonType string `json:"reasonType,omitempty"`
}

cadfReason := Reason{
	ReasonCode := ka.response.code + ": " + ka.response.reason
	ReasonType := "HTTP and Error"

}

// define outcome

if ka.response.code.string.startsWith('2')
cadfOutcome = "success"
else 
cadfOutcome = "failure"

//not used
//"unknown"
//"pending"


// define action

if req in ["CREATE"]
   cadfAction = "create"
if req in ["POST", "PATCH", "PUT"] 
   cadfAction = "update"
else if req in ["DELETE"]
   cadfAction = "delete"
if req in ["GET", "HEAD", "WATCH"]
   cadfAction = "read"





