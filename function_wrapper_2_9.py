import bmesh
import bpy


def do_bevel():
    bpy.ops.mesh.bevel(affect="EDGES", offset=0.0002)


def do_update_edit_mesh(m):
    bmesh.update_edit_mesh(m, False)
