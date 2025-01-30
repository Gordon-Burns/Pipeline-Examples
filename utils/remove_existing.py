def delete_existing(name,sch):
    job_names = sch.get_all(filter_text = name)
    pipeline_name = sch.get_all(filter_text = name)
    jobs_to_delete = [job for job in job_names if job.name == name]

    if jobs_to_delete:
        for job in jobs_to_delete:
            print(f"{job.name} Will be deleted")
        else:
            print(f"No existing jobs with name {name} found")

        jdr = [sch.delete_job(job) for job in jobs_to_delete]

    pipelines_to_delete = [pipe for pipe in pipeline_name if pipe.name == name]
    if pipelines_to_delete:
        for pipe in pipelines_to_delete:
            print(f"{pipe.name} Will be deleted")
            pdr = [sch.delete_pipeline(pipe) for pipe in pipelines_to_delete]
        else:
            print(f"No existing pipelines with name {name} found")

        