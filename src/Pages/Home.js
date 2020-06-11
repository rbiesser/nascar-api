import React from 'react'
import { Container, Item } from 'semantic-ui-react'
import Async from 'react-async';
import Parser from 'html-react-parser';

// https://www.npmjs.com/package/xml-js
var convert = require('xml-js');
var options = {
	compact: true, 
	ignoreComment: true, 
	spaces: 4,
	cdataFn: function(val) {
		return val
	}
}

const loadArticles = () =>
    fetch("https://www.nascar.com/json/articles/")
        .then(res => (res.ok ? res : Promise.reject(res)))
        .then(res => res.json())

export default function Home() {
    return (
        <Container>
            <Async promiseFn={loadArticles}>
                {({ data, err, isLoading }) => {
                    if (isLoading) return "Loading..."
                    if (err) return `Something went wrong: ${err.message}`

                    if (data)
                        return (
                            <Container style={{padding:'1rem'}}>
								<Item.Group link divided>
                                    {data.response.news.article.map(article => (
                                        <Item href={article.DesktopPath}>
											<Item.Image size='large' src={article['Main Image']} />
											<Item.Content>
												<Item.Header as='a'>{article.Heading}</Item.Header>
												<Item.Meta>{article.SubHead}</Item.Meta>
												<Item.Description content={
												Parser(
													JSON.parse(
														convert.xml2json(article.Introduction, options)
													)._cdata
												)} />
												<Item.Extra>{article['Publised Date']} by {article.Author}</Item.Extra>
											</Item.Content>
										</Item>
                                    ))}
								</Item.Group>
                            </Container>
                        )
                }}
            </Async>
        </Container>
    )
}