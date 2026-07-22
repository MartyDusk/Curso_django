#! /dev/null
#
echo "$(cat <<- 'EOF'
    django
    djangorestframework
    django-cors-headers
    djangorestframework_simplejwt
EOF
)" | xargs -P '1' sh -c "$(cat <<- 'EOF'
    VENV='/opt/venv'
    if [ '!' -d "${VENV:?}" ]; then {
        python -m 'venv' "${VENV:?}" && \
        "${VENV:?}/bin/pip" install --no-cache-dir "${@:?}"
    } fi
EOF
)" 'sh'