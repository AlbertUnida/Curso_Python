from http import HTTPStatus

from flask import Blueprint, jsonify, request

cliente_bp = Blueprint("cliente", __name__, url_prefix="/cliente")

# DB Clientes
CLIENTES = {
    "4133266": {
        "accion": "Success",
        "codRes": "SIN_ERROR",
        "menRes": "OK",
        "ci": "4133266",
        "nombre": "Derlis",
        "apellidos": "Caballero Mendoza",
        "cel": "0981111111",
        "dir": "San Blas",
    }
}


def _error_response(*, accion: str, men_res: str, ci, status: HTTPStatus):
    """Return a standard error payload for the cliente service."""
    payload = {
        "accion": accion,
        "codRes": "ERROR",
        "menRes": men_res,
        "ci": ci,
    }
    return jsonify(payload), status


@cliente_bp.post("")
def consultar_cliente():
    """REST endpoint to fetch client data by cedula."""
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return _error_response(
            accion="Debe informar la cedula",
            men_res="Datos incompletos",
            ci=None,
            status=HTTPStatus.BAD_REQUEST,
        )

    ci = str(payload.get("ci", "")).strip()

    if not ci:
        return _error_response(
            accion="Debe informar la cedula",
            men_res="Datos incompletos",
            ci=payload.get("ci"),
            status=HTTPStatus.BAD_REQUEST,
        )

    cliente = CLIENTES.get(ci)
    if cliente:
        return jsonify(cliente), HTTPStatus.OK

    return _error_response(
        accion="Cliente no esta en el sistema",
        men_res="Error cliente",
        ci=ci,
        status=HTTPStatus.NOT_FOUND,
    )
