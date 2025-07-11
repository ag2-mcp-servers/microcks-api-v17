# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T05:07:32+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Type(Enum):
    reqRespPair = 'reqRespPair'
    unidirEvent = 'unidirEvent'


class AbstractExchange(BaseModel):
    type: Type = Field(
        ..., description='Discriminant type for identifying kind of exchange'
    )


class ArtifactUpload(BaseModel):
    file: bytes = Field(..., description='The artifact to upload')


class Type1(Enum):
    KAFKA = 'KAFKA'
    MQTT = 'MQTT'
    WS = 'WS'
    AMQP = 'AMQP'
    NATS = 'NATS'
    GOOGLEPUBSUB = 'GOOGLEPUBSUB'


class Binding(BaseModel):
    destinationName: str = Field(
        ...,
        description='Name of destination for asynchronous messages of this operation',
    )
    destinationType: Optional[str] = Field(
        None,
        description='Type of destination for asynchronous messages of this operation',
    )
    keyType: Optional[str] = Field(None, description='Type of key for Kafka messages')
    method: Optional[str] = Field(None, description='HTTP method for WebSocket binding')
    persistent: Optional[bool] = Field(
        None, description='Persistent attribute for MQTT binding'
    )
    qoS: Optional[str] = Field(
        None, description='Quality of Service attribute for MQTT binding'
    )
    type: Type1 = Field(..., description='Protocol binding identifier')


class Counter(BaseModel):
    counter: Optional[int] = Field(
        None, description='Number of items in a resource collection'
    )


class CounterMap(RootModel[Optional[Dict[str, float]]]):
    root: Optional[Dict[str, float]] = None


class DailyInvocationStatistic(BaseModel):
    dailyCount: float = Field(
        ..., description='The number of service mock invocations on this day'
    )
    day: str = Field(
        ...,
        description='The day (formatted as yyyyMMdd string) represented by this statistic',
    )
    hourlyCount: Optional[Dict[str, Any]] = Field(
        None,
        description='The number of service mock invocations per hour of the day (keys range from 0 to 23)',
    )
    id: str = Field(..., description='Unique identifier of this statistic object')
    minuteCount: Optional[Dict[str, Any]] = Field(
        None,
        description='The number of service mock invocations per minute of the day (keys range from 0 to 1439)',
    )
    serviceName: str = Field(
        ..., description='The name of the service this statistic is related to'
    )
    serviceVersion: str = Field(
        ..., description='The version of the service this statistic is related to'
    )


class AsyncApi(BaseModel):
    default_binding: Optional[str] = Field(None, alias='default-binding')
    enabled: Optional[str] = None
    endpoint_AMQP: Optional[str] = Field(None, alias='endpoint-AMQP')
    endpoint_GOOGLEPUBSUB: Optional[str] = Field(None, alias='endpoint-GOOGLEPUBSUB')
    endpoint_KAFKA: Optional[str] = Field(None, alias='endpoint-KAFKA')
    endpoint_MQTT: Optional[str] = Field(None, alias='endpoint-MQTT')
    endpoint_NATS: Optional[str] = Field(None, alias='endpoint-NATS')
    endpoint_WS: Optional[str] = Field(None, alias='endpoint-WS')
    frequencies: Optional[str] = None


class MicrocksHub(BaseModel):
    allowed_roles: Optional[str] = Field(None, alias='allowed-roles')
    enabled: Optional[str] = None
    endpoint: Optional[str] = None


class RepositoryFilter(BaseModel):
    enabled: Optional[str] = None
    label_key: Optional[str] = Field(None, alias='label-key')
    label_label: Optional[str] = Field(None, alias='label-label')
    label_list: Optional[str] = Field(None, alias='label-list')


class RepositoryTenancy(BaseModel):
    artifact_import_allowed_roles: Optional[str] = Field(
        None, alias='artifact-import-allowed-roles'
    )
    enabled: Optional[str] = None


class FeaturesConfig(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    async_api: Optional[AsyncApi] = Field(
        None, alias='async-api', description='Asynchronous feature properties'
    )
    microcks_hub: Optional[MicrocksHub] = Field(
        None, alias='microcks-hub', description='Microcks Hub feature properties'
    )
    repository_filter: Optional[RepositoryFilter] = Field(
        None,
        alias='repository-filter',
        description='Repository filtering feature properties',
    )
    repository_tenancy: Optional[RepositoryTenancy] = Field(
        None,
        alias='repository-tenancy',
        description='Repository tenancy feature properties',
    )


class Header(BaseModel):
    name: str = Field(..., description='Unique distinct name of this Header')
    values: List[str] = Field(..., description='Values for this Header')


class HeaderDTO(BaseModel):
    name: str = Field(..., description='Unique distinct name of this Header')
    values: str = Field(
        ..., description='Values for this header (comma separated strings)'
    )


class SslRequired(Enum):
    none = 'none'
    external = 'external'


class KeycloakConfig(BaseModel):
    auth_server_url: str = Field(
        ..., alias='auth-server-url', description='SSO Server authentication url'
    )
    enabled: bool = Field(
        ..., description='Whether Keycloak authentification and usage is enabled'
    )
    public_client: str = Field(
        ...,
        alias='public-client',
        description='Name of public-client that can be used for requesting OAuth token',
    )
    realm: str = Field(..., description='Authentication realm name')
    resource: str = Field(
        ..., description='Name of Keycloak resource/application used on client side'
    )
    ssl_required: SslRequired = Field(
        ..., alias='ssl-required', description='SSL certificates requirements'
    )


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None, description='Annotations of attached object'
    )
    createdOn: int = Field(..., description='Creation date of attached object')
    labels: Optional[Dict[str, str]] = Field(
        None, description='Labels put on attached object'
    )
    lastUpdate: int = Field(..., description='Last update of attached object')


class OperationHeaders(RootModel[Optional[Dict[str, List[HeaderDTO]]]]):
    root: Optional[Dict[str, List[HeaderDTO]]] = None


class In(Enum):
    path = 'path'
    query = 'query'
    header = 'header'


class ParameterConstraint(BaseModel):
    in_: Optional[In] = Field(None, alias='in', description='Parameter location')
    mustMatchRegexp: Optional[str] = Field(
        None, description="Whether it's a regular expression matching constraint"
    )
    name: str = Field(..., description='Parameter name')
    recopy: Optional[bool] = Field(None, description="Whether it's a recopy constraint")
    required: Optional[bool] = Field(
        None, description="Whether it's a required constraint"
    )


class Request(BaseModel):
    content: Optional[str] = Field(None, description='Body content for this request')
    headers: Optional[List[Header]] = Field(
        None, description='Headers for this Request'
    )
    id: Optional[str] = Field(None, description='Unique identifier of Request')
    name: str = Field(..., description='Unique distinct name of this Request')
    operationId: str = Field(
        ..., description='Identifier of Operation this Request is associated to'
    )
    testCaseId: Optional[str] = Field(
        None,
        description='Unique identifier of TestCase this Request is attached (in case of a test)',
    )


class ResourceType(Enum):
    WSDL = 'WSDL'
    XSD = 'XSD'
    JSON_SCHEMA = 'JSON_SCHEMA'
    OPEN_API_SPEC = 'OPEN_API_SPEC'
    OPEN_API_SCHEMA = 'OPEN_API_SCHEMA'
    ASYNC_API_SPEC = 'ASYNC_API_SPEC'
    ASYNC_API_SCHEMA = 'ASYNC_API_SCHEMA'
    AVRO_SCHEMA = 'AVRO_SCHEMA'
    PROTOBUF_SCHEMA = 'PROTOBUF_SCHEMA'
    PROTOBUF_DESCRIPTION = 'PROTOBUF_DESCRIPTION'
    GRAPHQL_SCHEMA = 'GRAPHQL_SCHEMA'


class Response(BaseModel):
    content: Optional[str] = Field(None, description='Body content of this Response')
    headers: Optional[List[Header]] = Field(
        None, description='Headers for this Response'
    )
    id: Optional[str] = Field(None, description='Unique identifier of Response')
    name: str = Field(..., description='Unique distinct name of this Response')
    operationId: str = Field(
        ..., description='Identifier of Operation this Response is associated to'
    )
    testCaseId: Optional[str] = Field(
        None,
        description='Unique identifier of TestCase this Response is attached (in case of a test)',
    )


class Secret(BaseModel):
    caCertPem: Optional[str] = None
    description: str = Field(..., description='Description of this Secret')
    id: Optional[str] = Field(None, description='Unique identifier of Secret')
    name: str = Field(..., description='Unique distinct name of Secret')
    password: Optional[str] = None
    token: Optional[str] = None
    tokenHeader: Optional[str] = None
    username: Optional[str] = None


class SecretRef(BaseModel):
    name: str = Field(..., description='Distinct name of the referenced Secret')
    secretId: str = Field(..., description='Unique identifier or referenced Secret')


class Type2(Enum):
    REST = 'REST'
    SOAP_HTTP = 'SOAP_HTTP'
    GENERIC_REST = 'GENERIC_REST'
    GENERIC_EVENT = 'GENERIC_EVENT'
    EVENT = 'EVENT'
    GRPC = 'GRPC'
    GRAPHQL = 'GRAPHQL'


class ServiceRef(BaseModel):
    name: str = Field(..., description='The Service name')
    serviceId: str = Field(..., description='Unique reference of a Service')
    version: str = Field(..., description='The Service version')


class SnapshotUpload(BaseModel):
    file: bytes = Field(..., description='The repository snapshot file')


class StringArray(RootModel[List[str]]):
    root: List[str] = Field(..., description='A simple array of String')


class TestCaseReturnDTO(BaseModel):
    operationName: str = Field(
        ..., description='Name of related operation for this TestCase'
    )


class TestResultSummary(BaseModel):
    id: str = Field(..., description='Unique identifier of TestResult')
    serviceId: str = Field(..., description='Unique identifier of service tested')
    success: bool = Field(..., description='Flag telling if test is a success')
    testDate: int = Field(..., description='Timestamp of creation date of this service')


class TestRunnerType(Enum):
    HTTP = 'HTTP'
    SOAP_HTTP = 'SOAP_HTTP'
    SOAP_UI = 'SOAP_UI'
    POSTMAN = 'POSTMAN'
    OPEN_API_SCHEMA = 'OPEN_API_SCHEMA'
    ASYNC_API_SCHEMA = 'ASYNC_API_SCHEMA'
    GRPC_PROTOBUF = 'GRPC_PROTOBUF'
    GRAPHQL_SCHEMA = 'GRAPHQL_SCHEMA'


class TestStepResult(BaseModel):
    elapsedTime: Optional[float] = Field(
        None, description='Elapsed time in milliseconds since the test step beginning'
    )
    eventMessageName: Optional[str] = Field(
        None, description='Name of event this test step is bound to'
    )
    message: Optional[str] = Field(
        None, description='Error message that may be associated to this test step'
    )
    requestName: Optional[str] = Field(
        None, description='Name of request this test step is bound to'
    )
    success: bool = Field(..., description='Flag telling if test case is a success')


class Trend(Enum):
    DOWN = 'DOWN'
    LOW_DOWN = 'LOW_DOWN'
    STABLE = 'STABLE'
    LOW_UP = 'LOW_UP'
    UP = 'UP'


class WeightedMetricValue(BaseModel):
    name: str = Field(..., description='Metric name or serie name')
    value: int = Field(..., description='The value of this metric')
    weight: int = Field(
        ..., description='Weight of this metric value (typically a percentage)'
    )


class ServiceIds(RootModel[List[str]]):
    root: List[str]


class MetricsConformanceAggregateGetResponse(RootModel[List[WeightedMetricValue]]):
    root: List[WeightedMetricValue]


class MetricsInvocationsTopGetResponse(RootModel[List[DailyInvocationStatistic]]):
    root: List[DailyInvocationStatistic]


class MetricsTestsLatestGetResponse(RootModel[List[TestResultSummary]]):
    root: List[TestResultSummary]


class SecretsGetResponse(RootModel[List[Secret]]):
    root: List[Secret]


class QueryMap(RootModel[Optional[Dict[str, str]]]):
    root: Optional[Dict[str, str]] = None


class EventMessage(BaseModel):
    content: Optional[str] = Field(None, description='Body content for this message')
    headers: Optional[List[Header]] = Field(
        None, description='Headers for this message'
    )
    id: str = Field(..., description='Unique identifier of this message')
    mediaType: str = Field(..., description='Content type of message')
    name: Optional[str] = Field(
        None, description='Unique distinct name of this message'
    )
    operationId: Optional[str] = Field(
        None, description='Identifier of Operation this message is associated to'
    )
    testCaseId: Optional[str] = Field(
        None,
        description='Unique identifier of TestCase this message is attached (in case of a test)',
    )


class ImportJob(BaseModel):
    active: Optional[bool] = Field(
        None,
        description='Whether this ImportJob is active (ie. scheduled for execution)',
    )
    createdDate: Optional[datetime] = Field(
        None, description='Creation date for this ImportJob'
    )
    etag: Optional[str] = Field(
        None,
        description='Etag of repository URL during previous import. Is used for not re-importing if no recent changes',
    )
    frequency: Optional[str] = Field(None, description='Reserved for future usage')
    id: Optional[str] = Field(None, description='Unique identifier of ImportJob')
    lastImportDate: Optional[datetime] = Field(
        None, description='Date last import was done'
    )
    lastImportError: Optional[str] = Field(
        None, description='Error message of last import (if any)'
    )
    mainArtifact: Optional[bool] = Field(
        None,
        description='Flag telling if considered as primary or secondary artifact. Default to `true`',
    )
    metadata: Optional[Metadata] = Field(None, description='Metadata of ImportJob')
    name: str = Field(..., description='Unique distinct name of this ImportJob')
    repositoryDisableSSLValidation: Optional[bool] = Field(
        None,
        description='Whether to disable SSL certificate verification when checking repository',
    )
    repositoryUrl: str = Field(
        ..., description='URL of mocks and tests repository artifact'
    )
    secretRef: Optional[SecretRef] = Field(
        None, description='Reference of a Secret to used when checking repository'
    )
    serviceRefs: Optional[List[ServiceRef]] = Field(
        None, description='References of Services discovered when checking repository'
    )


class LabelsMap(RootModel[Optional[Dict[str, StringArray]]]):
    root: Optional[Dict[str, StringArray]] = None


class Operation(BaseModel):
    bindings: Optional[Dict[str, Binding]] = Field(
        None, description='Map of protocol binding details for this operation'
    )
    defaultDelay: Optional[float] = Field(
        None, description='Default response time delay for mocks'
    )
    dispatcher: Optional[str] = Field(
        None, description='Dispatcher strategy used for mocks'
    )
    dispatcherRules: Optional[str] = Field(
        None, description='DispatcherRules used for mocks'
    )
    inputName: Optional[str] = Field(
        None, description='Name of input parameters in case of Xml based Service'
    )
    method: str = Field(..., description='Represents transport method')
    name: str = Field(
        ..., description='Unique name of this Operation within Service scope'
    )
    outputName: Optional[str] = Field(
        None, description='Name of output parameters in case of Xml based Service'
    )
    parameterContraints: Optional[List[ParameterConstraint]] = Field(
        None,
        description='Contraints that may apply to mock invocatino on this operation',
    )
    resourcePaths: Optional[List[str]] = Field(
        None, description='Paths the mocks endpoints are mapped on'
    )


class OperationOverrideDTO(BaseModel):
    defaultDelay: Optional[int] = Field(
        None,
        description='Default delay in milliseconds to apply to mock responses on this operation',
    )
    dispatcher: Optional[str] = Field(
        None, description='Type of dispatcher to apply for this operation'
    )
    dispatcherRules: Optional[str] = Field(
        None, description='Rules of dispatcher for this operation'
    )
    parameterConstraints: Optional[List[ParameterConstraint]] = Field(
        None,
        description='Constraints that may apply to incoming parameters on this operation',
    )


class RequestResponsePair(AbstractExchange):
    request: Request = Field(..., description='The request part of the pair')
    response: Response = Field(..., description='The Response part of the pair')
    type: Literal['reqRespPair']


class Resource(BaseModel):
    content: str = Field(..., description='String content of this resource')
    id: str = Field(
        ..., description='Uniquer identifier of this Service or API Resource'
    )
    name: str = Field(
        ...,
        description='Unique name/business identifier for this Service or API resource',
    )
    path: Optional[str] = Field(
        None, description='Relatvie path of this resource regarding main resource'
    )
    serviceId: str = Field(
        ...,
        description='Unique identifier of the Servoce or API this resource is attached to',
    )
    sourceArtifact: Optional[str] = Field(
        None, description='Short name of the artifact this resource was extracted from'
    )
    type: ResourceType = Field(..., description='Type of this Service or API resource')


class Service(BaseModel):
    id: Optional[str] = Field(
        None, description='Unique identifier for this Service or API'
    )
    metadata: Optional[Metadata] = Field(None, description='Metadata of Service')
    name: str = Field(
        ...,
        description='Distinct name for this Service or API (maybe shared among many versions)',
    )
    operations: Optional[List[Operation]] = Field(
        None, description='Set of Operations for Service or API'
    )
    type: Type2 = Field(..., description='Service or API Type')
    version: str = Field(..., description='Distinct version for a named Service or API')
    xmlNS: Optional[str] = Field(
        None, description='Associated Xml Namespace in case of Xml based Service'
    )


class TestCaseResult(BaseModel):
    elapsedTime: float = Field(
        ..., description='Elapsed time in milliseconds since the test case beginning'
    )
    operationName: str = Field(
        ..., description='Name of operation this test case is bound to'
    )
    success: bool = Field(..., description='Flag telling if test case is a success')
    testStepResults: Optional[List[TestStepResult]] = Field(
        None, description='Test steps associated to this test case'
    )


class TestConformanceMetric(BaseModel):
    aggregationLabelValue: Optional[str] = Field(
        None, description='Value of the label used for metrics aggregation (if any)'
    )
    currentScore: float = Field(
        ..., description='Current test conformance score for the related Service'
    )
    id: str = Field(..., description='Unique identifier of coverage metric')
    lastUpdateDay: Optional[str] = Field(
        None, description='The day of latest score update (in yyyyMMdd format)'
    )
    latestScores: Optional[Dict[str, float]] = Field(
        None,
        description='History of latest scores (key is date with format yyyyMMdd, value is score as double)',
    )
    latestTrend: Optional[Trend] = Field(
        None, description='Evolution trend of currentScore'
    )
    maxPossibleScore: float = Field(
        ...,
        description='Maximum conformance score that can be reached (depends on samples expresiveness)',
    )
    serviceId: str = Field(
        ..., description='Unique identifier of the Service this metric is related to'
    )


class TestRequest(BaseModel):
    filteredOperations: Optional[List[str]] = Field(
        None, description='A restriction on service operations to test'
    )
    operationHeaders: Optional[OperationHeaders] = Field(
        None, description='This test operations headers override'
    )
    runnerType: TestRunnerType = Field(..., description='Runner used for this test')
    secretName: Optional[str] = Field(
        None, description='The name of Secret to use for connecting the test endpoint'
    )
    serviceId: str = Field(..., description='Unique identifier of service to test')
    testEndpoint: str = Field(..., description='Endpoint to test for this service')
    timeout: int = Field(
        ..., description='The maximum time (in milliseconds) to wait for this test ends'
    )


class TestResult(BaseModel):
    elapsedTime: Optional[float] = Field(
        None, description='Elapsed time in milliseconds since test beginning'
    )
    id: str = Field(..., description='Unique identifier of TestResult')
    inProgress: bool = Field(
        ..., description='Flag telling is test is still in progress'
    )
    operationHeaders: Optional[OperationHeaders] = Field(
        None, description='This test operations headers override'
    )
    runnerType: TestRunnerType = Field(..., description='Runner used for this test')
    secretRef: Optional[SecretRef] = Field(
        None,
        description='The referrence of the Secret used for connecting to test endpoint',
    )
    serviceId: str = Field(..., description='Unique identifier of service tested')
    success: bool = Field(..., description='Flag telling if test is a success')
    testCaseResults: Optional[List[TestCaseResult]] = Field(
        None, description='TestCase results associated to this test'
    )
    testDate: int = Field(..., description='Timestamp of creation date of this service')
    testNumber: float = Field(
        ..., description='Incremental number for tracking number of tests of a service'
    )
    testedEndpoint: str = Field(..., description='Endpoint used during test')
    timeout: Optional[int] = Field(
        None,
        description='The maximum time (in milliseconds) to wait for this test ends',
    )
    version: float = Field(..., description='Revision number of this test')


class TestReturn(BaseModel):
    code: int = Field(
        ..., description='Return code for test (0 means Success, 1 means Failure)'
    )
    elapsedTime: int = Field(..., description='Elapsed time in milliseconds')
    eventMessage: Optional[EventMessage] = Field(
        None, description='Event Message received for this test'
    )
    message: Optional[str] = Field(None, description='Error message if any')
    request: Optional[Request] = Field(None, description='Request sent for this test')
    response: Optional[Response] = Field(
        None, description='Response returned for this test'
    )


class UnidirectionalEvent(AbstractExchange):
    eventMessage: EventMessage = Field(
        ..., description='Asynchronous message for this unidirectional event'
    )
    type: Literal['unidirEvent']


class JobsGetResponse(RootModel[List[ImportJob]]):
    root: List[ImportJob]


class ResourcesServiceServiceIdGetResponse(RootModel[List[Resource]]):
    root: List[Resource]


class ServicesSearchGetResponse(RootModel[List[Service]]):
    root: List[Service]


class TestsServiceServiceIdGetResponse(RootModel[List[TestResult]]):
    root: List[TestResult]


class TestsIdEventsTestCaseIdGetResponse(RootModel[List[UnidirectionalEvent]]):
    root: List[UnidirectionalEvent]


class TestsIdMessagesTestCaseIdGetResponse(RootModel[List[RequestResponsePair]]):
    root: List[RequestResponsePair]


class Exchange(RootModel[Union[RequestResponsePair, UnidirectionalEvent]]):
    root: Union[RequestResponsePair, UnidirectionalEvent] = Field(
        ...,
        description='Abstract representation of a Service or API exchange type (request/response, event based, ...)',
        discriminator='type',
    )


class MessageArray(RootModel[List[Exchange]]):
    root: List[Exchange] = Field(
        ..., description='Array of Message for Service operations'
    )


class ServiceView(BaseModel):
    messagesMap: Dict[str, MessageArray] = Field(
        ...,
        description='Map of messages for this Service. Keys are operation name, values are array of messages for this operation',
    )
    service: Service = Field(..., description='Wrapped service description')


class ServicesIdGetResponse(RootModel[Union[Service, ServiceView]]):
    root: Union[Service, ServiceView]
