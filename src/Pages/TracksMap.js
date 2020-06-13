import React from 'react'
// import { Container, Header, Card } from 'semantic-ui-react'
// import Async from 'react-async';
import mapboxgl from 'mapbox-gl';
import './TracksMap.css'
import data from './TrackData.json'

mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_ACCESS_TOKEN;

export default class TracksMap extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lng: -95,
      lat: 39,
      zoom: 4
    };
  }

  componentDidMount() {
    const map = new mapboxgl.Map({
      container: this.mapContainer,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [this.state.lng, this.state.lat],
      zoom: this.state.zoom
    });

    map.on('move', () => {
      this.setState({
        lng: map.getCenter().lng.toFixed(4),
        lat: map.getCenter().lat.toFixed(4),
        zoom: map.getZoom().toFixed(2)
      });
    });

    map.on('load', () => {
      map.addSource('points', {
        type: 'geojson',
        data
      });
      map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'points',
        'layout': {
          // get the icon name from the source's "icon" property
          // concatenate the name to get an icon from the style's sprite sheet
          // 'icon-image': ['concat', ['get', 'icon'], '-15'],
          // get the title name from the source's "title" property
          'text-field': ['get', 'title'],
          'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
          'text-offset': [0, 0.6],
          'text-anchor': 'top'
        }
      });
    });
  }

  render() {
    return (
      <div>
        <div className='sidebarStyle'>
          <div>Longitude: {this.state.lng} | Latitude: {this.state.lat} | Zoom: {this.state.zoom}</div>
        </div>
        <div ref={el => this.mapContainer = el} className='mapContainer' />
      </div>
    )
  }
}

// const loadTracks = () =>
// 	fetch("https://www.nascar.com/json/tracks/")
// 		.then(res => (res.ok ? res : Promise.reject(res)))
// 		.then(res => res.json())

// export default function TracksMap() {
// 	return (
// 		<Container>
// 			<Async promiseFn={loadTracks}>
// 				{({ data, err, isLoading }) => {
// 					if (isLoading) return "Loading..."
// 					if (err) return `Something went wrong: ${err.message}`

// 					if (data)
// 						return (
// 							<div>
// 								<div>
// 									<Header as='h1' content='Tracks' />
// 								</div>
// 								<Card.Group itemsPerRow={5} doubling>
// 									{data.items.map(track => (
// 										<Card
// 											href={track.track_url}
// 											// image={driver.Image}
// 											header={track.track_name}
// 											meta={`Year Built: ${track.year_built}`}
// 											description={`${track.city}, ${track.state}`}
// 											extra={track.track_type}
// 										/>
// 									))}
// 								</Card.Group>
// 							</div>
// 						)
// 				}}
// 			</Async>
// 		</Container>
// 	)
// }