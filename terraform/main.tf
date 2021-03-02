provider "google" {
  project = "southern-unity-304118"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "static-site" {
  name          = "test-bucket-farid"
  force_destroy = true

  uniform_bucket_level_access = true

}