from aws_cdk import (
  Stack,
  aws_lambda as _lambda, # Import the Lambda module
  CfnOutput,
  # Import API Gateway L2 construct
    aws_apigateway as apigateway
)
from constructs import Construct

class CdkInfraStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    hello_world_function = _lambda.Function(
            self,
            "HelloWorldFunction",
            runtime = _lambda.Runtime.NODEJS_20_X, # Choose any supported Node.js runtime
            code = _lambda.Code.from_asset("lambda"), # Points to the lambda directory
            handler = "hello.handler", # Points to the 'hello' file in the lambda directory
        )
    
    # Define the API Gateway resource
    api = apigateway.LambdaRestApi(
        self,
        "HelloWorldApi",
        handler = hello_world_function,
        proxy = False,
    )
    
    # Define the '/hello' resource with a GET method
    hello_resource = api.root.add_resource("hello")
    hello_resource.add_method("GET")
    
    # # Define the Lambda function resource
    # my_function = _lambda.Function(
    #   self, "HelloWorldFunction", 
    #   runtime = _lambda.Runtime.NODEJS_20_X, # Provide any supported Node.js runtime
    #   handler = "index.handler",
    #   code = _lambda.Code.from_inline(
    #     """
    #     exports.handler = async function(event) {
    #       return {
    #         statusCode: 200,
    #         body: JSON.stringify('You are now seeing this code'),
    #       };
    #     };
    #     """
    #   ),
    # )

    # # Define the Lambda function URL resource
    # my_function_url = my_function.add_function_url(
    #   auth_type = _lambda.FunctionUrlAuthType.NONE,
    # )

    # # Define a CloudFormation output for your URL
    # CfnOutput(self, "myFunctionUrlOutput", value=my_function_url.url)