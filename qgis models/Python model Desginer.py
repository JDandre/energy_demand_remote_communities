"""
Model exported as python.
Name : Add parameters to communities
Group : 
With QGIS : 31803
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterString
from qgis.core import QgsProcessingParameterFeatureSink
from qgis.core import QgsProcessingParameterFileDestination
import processing


class AddParametersToCommunities(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('InputvectorLayer', 'Building_polygons', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterString('InputstringCRS', 'Input_string_CRS_', multiLine=False, defaultValue='EPSG:5931'))
        self.addParameter(QgsProcessingParameterFileDestination('FilePath', 'File path', fileFilter='Microsoft Excel (*.xlsx);;Open Document Spreadsheet (*.ods)', createByDefault=True, defaultValue=None))
        

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(19, model_feedback)
        results = {}
        outputs = {}

        # Reproject layer
        alg_params = {
            'INPUT': parameters['InputvectorLayer'],
            'OPERATION': '',
            'TARGET_CRS': parameters['InputstringCRS'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReprojectLayer'] = processing.run('native:reprojectlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Refactor fields
        alg_params = {
            'FIELDS_MAPPING': [
            {'expression': '"osm_id"','length': 254,'name': 'osm_id','precision': 0,'type': 10},
            {'expression': 'x(centroid($geometry))','length': 0,'name': 'centroid_x','precision': 0,'type': 6},
            {'expression': 'y(centroid($geometry))','length': 0,'name': 'centroid_y','precision': 0,'type': 6},
            {'expression': 'area($geometry)','length': 20,'name': 'area','precision': 6,'type': 6},
            {'expression': 'perimeter($geometry)','length': 20,'name': 'perimeter','precision': 6,'type': 6},
            {'expression': 'perimeter($geometry) / (sqrt(area($geometry))*4)','length': 20,'name': 'shape_index','precision': 6,'type': 6},
            {'expression': 'perimeter(convex_hull($geometry))','length': 0,'name': 'detour','precision': 0,'type': 6},
            {'expression': 'perimeter($geometry) / perimeter(convex_hull($geometry))','length': 0,'name': 'detour_index','precision': 0,'type': 6},
            {'expression': 'sqrt( area(minimal_circle( $geometry)) / pi()) *2','length': 20,'name': 'range','precision': 6,'type': 6},
            {'expression': '(4 * (sqrt( area($geometry) / pi())))/ (sqrt( area(minimal_circle( $geometry)) / pi()) *2)','length': 20,'name': 'range_index','precision': 6,'type': 6},
            {'expression': 'bounds_width($geometry)','length': 20,'name': 'width','precision': 6,'type': 6},
            {'expression': 'bounds_height($geometry)','length': 20,'name': 'lengh','precision': 6,'type': 6},
            {'expression': 'num_points($geometry)','length': 20,'name': 'pnt_count','precision': 0,'type': 6},
            {'expression': 'area(intersection(make_circle( centroid($geometry), sqrt( area($geometry) / pi())), $geometry))','length': 20,'name': 'exchange','precision': 6,'type': 6},
            {'expression': '(area(intersection(make_circle( centroid($geometry), sqrt( area($geometry) / pi())), $geometry))) / area($geometry)','length': 20,'name': 'exchange_index','precision': 6,'type': 6},
            {'expression': 'perimeter($geometry) / perimeter(make_circle(centroid($geometry), sqrt( area($geometry) / pi())))','length': 20,'name': 'perimeter_index','precision': 6,'type': 6}
            
            ],
            
            'INPUT': outputs['ReprojectLayer']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RefactorFields'] = processing.run('native:refactorfields', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Quick_output'] = outputs['RefactorFields']['OUTPUT']
        
        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Export to spreadsheet
        alg_params = {
            'FORMATTED_VALUES': False,
            'LAYERS': outputs['RefactorFields']['OUTPUT'],
            'OVERWRITE': False,
            'USE_ALIAS': True,
            'OUTPUT': parameters['FilePath']
        }
        outputs['ExportToSpreadsheet'] = processing.run('native:exporttospreadsheet', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['FilePath'] = outputs['ExportToSpreadsheet']['OUTPUT']
        
        
        return results

    def name(self):
        return 'Add parameters to communities'

    def displayName(self):
        return 'Add parameters to communities'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return AddParametersToCommunities()
