terraform {
	// Ensures that everyone is using a specific Terraform version
	required_version = ">= 0.14.9"

  // Where Terraform stores its state to keep track of the resources it manages
	backend "s3" {
    bucket = "ssts-league-stats-terrform-state"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }

  // Declares providers, so that Terraform can install and use them
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }

    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }
}

// Specify settings for a given required provider
provider "aws" {
  region = "us-east-1"
}
