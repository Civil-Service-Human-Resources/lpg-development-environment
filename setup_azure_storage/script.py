from azure.storage.blob import BlobServiceClient, AccessPolicy, PublicAccess
from azure.core.exceptions import ResourceExistsError


CONTENT_CONTAINER="rustici"

blob_service_client = BlobServiceClient(
	account_url="http://azurite:9100/devstoreaccount1",
	credential={
		"account_name": "devstoreaccount1",
		"account_key": (
			"Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq"
			"/K1SZFPTOtr/KBHBeksoGMGw=="
		)
	}
)

if next(blob_service_client.list_containers(), None):
	print("Emulator already has required containers, will skip initialization.")
else:
	container_client = blob_service_client.get_container_client(CONTENT_CONTAINER)
	try:
		container_client.create_container()
		access_policy = AccessPolicy(permission=PublicAccess)
		container_client.set_container_access_policy(access_policy)
	except ResourceExistsError:
		pass
