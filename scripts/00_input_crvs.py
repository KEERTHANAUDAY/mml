"""Input node curves
   Pipe curves
"""
#Imports========================================================
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


#input==========================================================
node_curve_ids = rs.GetObjects("select_curves", 4)

input_start_radius=rs.GetReal("Pipe start radius")
input_end_radius=rs.GetReal("Pipe end radius")
tol=sc.doc.ModelAbsoluteTolerance
aTol=sc.doc.ModelAngleToleranceRadians

#build geometry
node_curves = []
for id in node_curve_ids:
    node_curve = rs.coercecurve(id)
    pipes = Rhino.Geometry.Brep.CreatePipe(node_curve,input_start_radius,False, 0, True,tol,aTol )
    for pipe in pipes:
        sc.doc.Objects.AddBrep(pipe)
    sc.doc.Views.Redraw()





