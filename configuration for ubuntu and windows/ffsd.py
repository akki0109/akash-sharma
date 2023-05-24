from subprocess import call

call(["ssh" , "-i" ,  "Downloads/test.pem" , "-o","StrictHostKeyChecking=no", "ubuntu@ec2-18-189-192-40.us-east-2.compute.amazonaws.com"])