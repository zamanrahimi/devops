provider "aws" {
  region = "us-west-2"  # Change this to your desired region
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "my-eks-cluster"
  cluster_version = "1.21"

  subnets = ["default"]  # Use default subnets in the default VPC

  node_groups = {
    eks_nodes = {
      desired_capacity = 1
      max_capacity     = 2
      min_capacity     = 1

      instance_type = "t3.small"
    }
  }
}
