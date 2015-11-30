from wtfpeewee.orm import model_form
from flask import Blueprint
from flask import render_template, redirect, request, url_for

from app.universal import get_object_or_404
from app.accounts.session import login_required
from app.groups.models import Group
from .models import Stud

bp = Blueprint('stud', __name__, template_folder='templates')

@bp.route('/<group_id>/create/', methods=['GET', 'POST'])
@login_required
def stud_create(group_id):
    StudForm = model_form(Stud)
    stud = Stud()
    if request.method == 'POST':
        form = StudForm(request.form)
        if form.validate():
            form.populate_obj(stud)
            stud.save()
            return redirect(url_for('group.studs_list', 
                                    group_id=group_id))
    else:
        stud.cgroup = get_object_or_404(Group, Group.id == group_id)
        form = StudForm(obj=stud)
    return render_template('students/stud_form.html', 
                            form=form, group_id=group_id)

@bp.route('/<stud_id>/edit/<group_id>/', methods=['GET', 'POST'])
@login_required
def stud_edit(stud_id, group_id):
    StudForm = model_form(Stud, field_args={'dbirthday': dict(format='%d.%m.%Y')})
    stud = get_object_or_404(Stud, Stud.id == stud_id)
    if request.method == 'POST':
        form = StudForm(request.form, obj=stud)
        if form.validate():
            form.populate_obj(stud)
            stud.save()
            return redirect(url_for('group.studs_list', 
                                    group_id=group_id))
    else:
        form = StudForm(obj=stud)
    return render_template('students/stud_form.html', 
                           form=form, stud=stud, group_id=group_id)

@bp.route('/<stud_id>/delete/<group_id>/', methods=['POST'])
@login_required
def stud_delete(stud_id, group_id):
    stud = get_object_or_404(Stud, Stud.id == stud_id)
    try:
        stud.delete_instance()
        return redirect(url_for('group.studs_list', 
                        group_id=group_id))
    except Exception as e:
        StudForm = model_form(Stud)
        form = StudForm(obj=stud)
        return render_template('students/stud_form.html', 
                     form=form, stud=stud, error_message=e)
