import React from 'react'
import './App.css'

/* Components */
import NavMenu from './Components/NavMenu'
import {
	HashRouter,
	Switch,
	Route
} from 'react-router-dom'
import { Container, Image } from 'semantic-ui-react'

/* Pages */
import Drivers from './Pages/Drivers'
import Tracks from './Pages/Tracks'
import Schedule from './Pages/Schedule'
import Standings from './Pages/Standings'
import Home from './Pages/Home'
import TracksMap from './Pages/TracksMap'

export default function App() {
		return (
			<Container>
				<HashRouter>
					<header>
						<Image src='https://m.nascar.com/wp-content/uploads/sites/7/2020/01/NASCAR_Barmark_Logo-1-2-1.svg' 
								alt="Official Site Of NASCAR" 
								size='medium' centered
						/>
						<NavMenu />
					</header>
					<main>
						<Switch>
							<Route path='/drivers' component={Drivers} />
							<Route path='/tracks/map' component={TracksMap} />
							<Route path='/tracks' component={Tracks} />
							<Route path='/schedule' component={Schedule} />
							<Route path='/standings' component={Standings} />
							<Route path='/' component={Home} />
						</Switch>
					</main>
					<footer>Copyright &copy; {new Date().getFullYear()} NASCAR&trade; | All Rights Reserved</footer>
				</HashRouter>
			</Container>
		);
	}