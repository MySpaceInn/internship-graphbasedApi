from .lib.validation_model import RecordModel,AttributeModel


record_models = [
    RecordModel(record_model="roster", attributes=[
        AttributeModel(name="year",validation=r"^-?\d+$", is_mandatory=True),
        AttributeModel(name="start_date",validation=r"^\d{4}-\d{2}-\d{2}$", is_mandatory=True),
        AttributeModel(name="end_date",validation=r"^\d{4}-\d{2}-\d{2}$", is_mandatory=True),
        AttributeModel(name="creator_name",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
    ]),
    RecordModel(record_model="business", attributes=[
        AttributeModel(name="registered_date",validation=r"^\d{4}-\d{2}-\d{2}$", is_mandatory=True),
        AttributeModel(name="tax_number",validation=r"^-?\d+$", is_mandatory=True),
        AttributeModel(name="owner_name",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="location", validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="business_name",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=False),
    ]),
    RecordModel(record_model="staff", attributes=[
        AttributeModel(name="tax_number", validation=r"^-?\d+$", is_mandatory=True),
        AttributeModel(name="address",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="age",validation=r"^-?\d+$", is_mandatory=True),
        AttributeModel(name="name", validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
     ]),
    RecordModel(record_model="allowance", attributes=[
        AttributeModel(name="type",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="date_issued",validation=r"^\d{4}-\d{2}-\d{2}$", is_mandatory=True),
        AttributeModel(name="address",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="amount",validation=r"^-?\d+(\.\d+)?$", is_mandatory=True),
        AttributeModel(name="name",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
    ]),
    RecordModel(record_model="leave", attributes=[
        AttributeModel(name="name",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="address",validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True),
        AttributeModel(name="duration",validation=r"^-?\d+$", is_mandatory=True),
        AttributeModel(name="type", validation=r"^[A-Za-z0-9\s]+$", is_mandatory=True)
    ])

]


