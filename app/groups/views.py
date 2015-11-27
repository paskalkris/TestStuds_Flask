from wtfpeewee.orm import model_form
from flask import g, Blueprint
from flask import render_template, redirect, url_for, request

from app.universal import get_object_or_404
from app.students.models import Stud
from .models import Group

bp = Blueprint('group', __name__, template_folder='templates')

@bp.route('/')
def groups_list():
    glist = Group.select().order_by(Group.name)
    #context = ['groups_list'=glist]
    template_name = 'groups/groups_list.html'
    return render_template(template_name, groups_list=glist)

@bp.route('/<group_id>/')
def studs_list(group_id):
    group = get_object_or_404(Group, Group.id == group_id)
    template_name = 'groups/studs_list.html'
    return render_template(template_name, group=group)

@bp.route('/create/', methods=['GET', 'POST'])
def group_create():
    GroupForm = model_form(Group)
    group = Group()
    if request.method == 'POST':
        form = GroupForm(request.form, obj=group)
        if form.validate():
            form.populate_obj(group)
            group.save()
            return redirect(url_for('group.groups_list'))
    else:
        form = GroupForm(obj=group)
    return render_template('groups/group_form.html', form=form)

@bp.route('/<group_id>/edit/', methods=['GET', 'POST'])
def group_edit(group_id):
    GroupForm = model_form(Group)
    group = get_object_or_404(Group, Group.id == group_id)
    if request.method == 'POST':
        form = GroupForm(request.form, obj=group)
        if form.validate():
            form.populate_obj(group)
            group.save()
            return redirect(url_for('group.groups_list'))
    else:
        form = GroupForm(obj=group)
        form.starosta.query = Stud.filter(cgroup=group)
    return render_template('groups/group_form.html', form=form, group=group)

@bp.route('/<group_id>/delete/', methods=['POST'])
def group_delete(group_id):
    group = get_object_or_404(Group, Group.id == group_id)
    try:
        group.delete_instance()
        return redirect(url_for('group.groups_list'))
    except Exception as e:
        return redirect(url_for('group.group_edit', group_id=group_id))

@bp.route('/<group_id>/confirm_delete', methods=['POST'])
def confirm_delete(group_id):
    group = get_object_or_404(Group, Group.id == group_id)
    template_name = 'groups/confirm_delete.html'
    return render_template(template_name, group=group)


@bp.route('/login')
def login():
    pass
