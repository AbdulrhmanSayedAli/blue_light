def auto_increment_generator(model, field_name):
    try:
        model_manager = model.all_objects if hasattr(model, "all_objects") else model.objects
        return getattr(model_manager.all().order_by(f"-{field_name}").first(), field_name, 0) + 1
    except:
        return 1
