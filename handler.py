import runpod

def handler(job):
    print(job)
    job_input = job["input"]  # Access the input from the request
    print("the job input is", job_input)
    # Add your custom code here
    return "Your job results"

runpod.serverless.start({"handler": handler})
