import os
import boto3

# Establecer las credenciales como variables de entorno (esto sigue siendo inseguro si tu código se comparte o almacena en un lugar inseguro).
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAY4UO3BBQSW6YEBI3'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

# A partir de aquí, boto3 utilizará automáticamente las credenciales establecidas en las variables de entorno.
ecs_client = boto3.client('ecs', region_name='us-east-1')

# Resto de tu código para trabajar con ECS...

def delete_ecs_clusters(region_name):
    # Crear un cliente de ECS en la región especificada
    ecs_client = boto3.client('ecs', region_name=region_name)

    # Obtener la lista de clusters
    clusters = ecs_client.list_clusters()['clusterArns']

    for cluster_arn in clusters:
        # Listar todos los servicios en el cluster
        services = ecs_client.list_services(cluster=cluster_arn)['serviceArns']
        if services:
            # Actualizar los servicios para establecer el número deseado de tareas como 0
            for service_arn in services:
                ecs_client.update_service(cluster=cluster_arn, service=service_arn, desiredCount=0)
                # Esperar a que el servicio se actualice
                waiter = ecs_client.get_waiter('services_stable')
                waiter.wait(cluster=cluster_arn, services=[service_arn])
            # Eliminar los servicios
            for service_arn in services:
                ecs_client.delete_service(cluster=cluster_arn, service=service_arn, force=True)

        # Listar todas las tareas en el cluster
        tasks = ecs_client.list_tasks(cluster=cluster_arn)['taskArns']
        if tasks:
            # Detener las tareas
            for task_arn in tasks:
                ecs_client.stop_task(cluster=cluster_arn, task=task_arn)

        # Después de detener todos los servicios y tareas, eliminar el cluster
        ecs_client.delete_cluster(cluster=cluster_arn)

# Lista de todas las regiones de AWS a limpiar
aws_regions = [
    'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-northeast-3', 'ap-northeast-2',
    'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1',
    'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2',
    'eu-west-3', 'eu-north-1', 'sa-east-1'
]

for region in aws_regions:
    print(f"Deleting ECS clusters in {region}...")
    delete_ecs_clusters(region)