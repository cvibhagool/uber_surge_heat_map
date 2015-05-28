function getNbhLoc(features){
	var nbh_locations = {};

	for (i = 0;i < features.length;i++){
		neighborhood = features[i].properties.neighborho;
		coordinates = _.flatten(features[i].geometry.coordinates);
		y = [];
		x = [];
		for (j = 0;j < coordinates.length;j++){
			if (j % 2 == 0){
				x.push(coordinates[j]);
			}
			else{
				y.push(coordinates[j]);
			}
		}
		nbh_locations[neighborhood] = getCentriod(x,y);
	}
	return nbh_locations;
}

function getCentriod(x,y){
	x1 = _.min(x);
	y1 = _.min(y);
	x2 = _.max(x);
	y2 = _.max(y);
	center_x = x1 + ((x2 - x1)/2)
	center_y = y1 + ((y2 - y1)/2)

	return {x: center_x, y: center_y}
}