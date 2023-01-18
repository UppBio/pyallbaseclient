import sgqlc.types


allbase_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class Compartment(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Name')


class Compound(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'name', 'compartment', 'kegg_id', 'chemical_formula', 'inchi_string', 'casnumber')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Name')
    compartment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Compartment')
    kegg_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='KeggID')
    chemical_formula = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ChemicalFormula')
    inchi_string = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='InchiString')
    casnumber = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='CASNumber')


class FBAModel(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'file_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='FileName')


class Gene(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'name', 'type', 'model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Name')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Type')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')


class Model(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'file_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='FileName')


class ModelCompound(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('compund_id', 'model_id')
    compund_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='CompundID')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')


class ModelReaction(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('reaction_id', 'model_id', 'is_reversible')
    reaction_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ReactionID')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')
    is_reversible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='IsReversible')


class Protein(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'name', 'type', 'model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Name')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Type')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')


class Query(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('compounds', 'organisms', 'unique_metabolic_clusters', 'model_ids_from_cluster', 'all_model_ids', 'organism_name', 'organism_id', 'compound_id', 'like_compound_id', 'compound_idfrom_inchi', 'compound_inchi', 'compound_name_from_inchi', 'compound_name', 'compound_compartment', 'reaction_name', 'reaction_id', 'reaction_ids_from_compound', 'reaction_species', 'reactant_compound_ids', 'get_reactions_with_product', 'model_compounds', 'compound_ids', 'compound_inchi_strings', 'model_reactions', 'reaction_ids', 'reaction_reversibility', 'reaction_reversibility_global', 'reaction_gene_associations', 'reaction_protein_associations', 'stoichiometry', 'reaction_catalysts', 'compartment_id', 'reaction_solvents', 'reaction_temperature', 'reaction_pressure', 'reaction_time', 'reaction_yield', 'reaction_reference', 'reaction_by_type', 'reaction_type', 'reaction_keggids', 'reaction_keggid', 'compound_keggid', 'compound_keggids', 'chemical_formulas', 'chemical_formula', 'compound_casnumbers', 'compound_casnumber', 'compound_idby_formula', 'compound_name_by_search_term', 'moded_idby_file_name', 'fba_model_ids')
    compounds = sgqlc.types.Field(sgqlc.types.list_of(Compound), graphql_name='compounds')
    organisms = sgqlc.types.Field(sgqlc.types.list_of(Model), graphql_name='organisms')
    unique_metabolic_clusters = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='uniqueMetabolicClusters')
    model_ids_from_cluster = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='modelIDsFromCluster', args=sgqlc.types.ArgDict((
        ('cluster', sgqlc.types.Arg(String, graphql_name='cluster', default=None)),
))
    )
    all_model_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='allModelIDs')
    organism_name = sgqlc.types.Field(String, graphql_name='organismName', args=sgqlc.types.ArgDict((
        ('organism_id', sgqlc.types.Arg(String, graphql_name='organismID', default=None)),
))
    )
    organism_id = sgqlc.types.Field(String, graphql_name='organismID', args=sgqlc.types.ArgDict((
        ('organism_name', sgqlc.types.Arg(String, graphql_name='organismName', default=None)),
))
    )
    compound_id = sgqlc.types.Field(String, graphql_name='compoundID', args=sgqlc.types.ArgDict((
        ('compound_name', sgqlc.types.Arg(String, graphql_name='compoundName', default=None)),
))
    )
    like_compound_id = sgqlc.types.Field(String, graphql_name='likeCompoundID', args=sgqlc.types.ArgDict((
        ('compound_name', sgqlc.types.Arg(String, graphql_name='compoundName', default=None)),
))
    )
    compound_idfrom_inchi = sgqlc.types.Field(String, graphql_name='compoundIDFromInchi', args=sgqlc.types.ArgDict((
        ('inchi', sgqlc.types.Arg(String, graphql_name='inchi', default=None)),
))
    )
    compound_inchi = sgqlc.types.Field(String, graphql_name='compoundInchi', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    compound_name_from_inchi = sgqlc.types.Field(String, graphql_name='compoundNameFromInchi', args=sgqlc.types.ArgDict((
        ('inchi', sgqlc.types.Arg(String, graphql_name='inchi', default=None)),
))
    )
    compound_name = sgqlc.types.Field(String, graphql_name='compoundName', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    compound_compartment = sgqlc.types.Field(String, graphql_name='compoundCompartment', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    reaction_name = sgqlc.types.Field(String, graphql_name='reactionName', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_id = sgqlc.types.Field(String, graphql_name='reactionID', args=sgqlc.types.ArgDict((
        ('reaction_name', sgqlc.types.Arg(String, graphql_name='reactionName', default=None)),
))
    )
    reaction_ids_from_compound = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionIDsFromCompound', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
        ('is_product', sgqlc.types.Arg(Boolean, graphql_name='isProduct', default=None)),
))
    )
    reaction_species = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionSpecies', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reactant_compound_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactantCompoundIDs', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    get_reactions_with_product = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='getReactionsWithProduct', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    model_compounds = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='modelCompounds', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(String, graphql_name='modelID', default=None)),
))
    )
    compound_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundIDs')
    compound_inchi_strings = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundInchiStrings')
    model_reactions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='modelReactions', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(String, graphql_name='modelID', default=None)),
))
    )
    reaction_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionIDs')
    reaction_reversibility = sgqlc.types.Field(Boolean, graphql_name='reactionReversibility', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
        ('model_id', sgqlc.types.Arg(String, graphql_name='modelID', default=None)),
))
    )
    reaction_reversibility_global = sgqlc.types.Field(Boolean, graphql_name='reactionReversibilityGlobal', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_gene_associations = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionGeneAssociations', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
        ('model_id', sgqlc.types.Arg(String, graphql_name='modelID', default=None)),
))
    )
    reaction_protein_associations = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionProteinAssociations', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
        ('model_id', sgqlc.types.Arg(String, graphql_name='modelID', default=None)),
))
    )
    stoichiometry = sgqlc.types.Field(Float, graphql_name='stoichiometry', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
        ('is_product', sgqlc.types.Arg(Boolean, graphql_name='isProduct', default=None)),
))
    )
    reaction_catalysts = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionCatalysts', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    compartment_id = sgqlc.types.Field(String, graphql_name='compartmentID', args=sgqlc.types.ArgDict((
        ('compartment_name', sgqlc.types.Arg(String, graphql_name='compartmentName', default=None)),
))
    )
    reaction_solvents = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionSolvents', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_temperature = sgqlc.types.Field(Float, graphql_name='reactionTemperature', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_pressure = sgqlc.types.Field(Float, graphql_name='reactionPressure', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_time = sgqlc.types.Field(Float, graphql_name='reactionTime', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_yield = sgqlc.types.Field(Float, graphql_name='reactionYield', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_reference = sgqlc.types.Field(String, graphql_name='reactionReference', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_by_type = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionByType', args=sgqlc.types.ArgDict((
        ('reaction_type', sgqlc.types.Arg(String, graphql_name='reactionType', default=None)),
))
    )
    reaction_type = sgqlc.types.Field(String, graphql_name='reactionType', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    reaction_keggids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reactionKEGGIDs')
    reaction_keggid = sgqlc.types.Field(String, graphql_name='reactionKEGGID', args=sgqlc.types.ArgDict((
        ('reaction_id', sgqlc.types.Arg(String, graphql_name='reactionID', default=None)),
))
    )
    compound_keggid = sgqlc.types.Field(String, graphql_name='compoundKEGGID', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    compound_keggids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundKEGGIDs')
    chemical_formulas = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chemicalFormulas')
    chemical_formula = sgqlc.types.Field(String, graphql_name='chemicalFormula', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    compound_casnumbers = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundCASNumbers')
    compound_casnumber = sgqlc.types.Field(String, graphql_name='compoundCASNumber', args=sgqlc.types.ArgDict((
        ('compound_id', sgqlc.types.Arg(String, graphql_name='compoundID', default=None)),
))
    )
    compound_idby_formula = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundIDByFormula', args=sgqlc.types.ArgDict((
        ('formula', sgqlc.types.Arg(String, graphql_name='formula', default=None)),
))
    )
    compound_name_by_search_term = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='compoundNameBySearchTerm', args=sgqlc.types.ArgDict((
        ('search_term', sgqlc.types.Arg(String, graphql_name='searchTerm', default=None)),
))
    )
    moded_idby_file_name = sgqlc.types.Field(String, graphql_name='modedIDByFileName', args=sgqlc.types.ArgDict((
        ('file_name', sgqlc.types.Arg(String, graphql_name='fileName', default=None)),
))
    )
    fba_model_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fbaModelIDs')


class Reaction(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('id', 'name', 'kegg_id', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Name')
    kegg_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='KeggID')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='Type')


class ReactionCompound(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('reaction_id', 'compound_id', 'is_product', 'stochiometry', 'file_numer')
    reaction_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ReactionID')
    compound_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='CompoundID')
    is_product = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='IsProduct')
    stochiometry = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='Stochiometry')
    file_numer = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='FileNumer')


class ReactionGene(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('reaction_id', 'model_id', 'gene_id')
    reaction_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ReactionID')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')
    gene_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='GeneID')


class ReactionProtein(sgqlc.types.Type):
    __schema__ = allbase_schema
    __field_names__ = ('reaction_id', 'model_id', 'protein_id')
    reaction_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ReactionID')
    model_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ModelID')
    protein_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ProteinID')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
allbase_schema.query_type = Query
allbase_schema.mutation_type = None
allbase_schema.subscription_type = None

