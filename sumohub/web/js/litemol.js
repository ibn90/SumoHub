let plugin = LiteMol.Plugin.create({ 
    target: document.getElementById('litemol'),
    viewportBackground: '#ffffff',
    layoutState: { hideControls: true } // you can also include isExpanded: true
});
plugin.context.logger.message(`Hello LiteMol`);


Transformer = LiteMol.Bootstrap.Entity.Transformer
let id = '1cbs';
let action = plugin.createTransform();
    
action.add(plugin.root, Transformer.Data.Download, 
        { url: `https://www.ebi.ac.uk/pdbe/static/entry/${id}_updated.cif`, type: 'String', id })
    .then(Transformer.Data.ParseCif, { id }, { isBinding: true })
    .then(Transformer.Molecule.CreateFromMmCif, { blockIndex: 0 })
    .then(Transformer.Molecule.CreateModel, { modelIndex: 0 })
    .then(Transformer.Molecule.CreateMacromoleculeVisual, { polymer: true, het: true, water: false });

plugin.applyTransform(action);