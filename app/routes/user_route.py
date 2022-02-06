from flask import Blueprint, make_response

from app.models import UserModel, AddressModel

from app.database import session


user_route = Blueprint("user_route", __name__, url_prefix="/user")


@user_route.route("/", methods=["GET"])
def user_index():

    # user = (
    #     session.query(UserModel)
    #     .filter_by(_UserModel__email="basicblogtalk@gmail.com")
    #     .one()
    # )

    # print(user.address.address1)

    address = session.query(AddressModel).filter(AddressModel.user_id == 2).one()

    print(address.user)

    return make_response({"data": f"{address.user.first_name} {address.user.last_name}"}, 200)


@user_route.route("/create", methods=["GET"])
def user_create():

    new_user = UserModel(
        {"first_name": "Kimsea", "last_name": "Sok", "email": "basicblogtalk@gmail.com"}
    )

    new_user.set_password("my_password")

    new_address = AddressModel(
        {
            "address1": "National Highway #6",
            "address2": "Phumbey, Preah Ponlea",
            "city": "Sereisophon",
            "state": "BMC",
            "country": "Cambodia",
        }
    )

    new_user.address = new_address

    session.add(new_user)

    session.commit()

    return make_response({"message": "create success"}, 200)
