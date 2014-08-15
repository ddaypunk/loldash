/** @jsx React.DOM */

require(['vendor/react', 'vendor/reqwest'], function (React, reqwest) {

React.renderComponent(
    <SummonerList url="/api/summoners/" />,
    document.getElementById('content')
);

});

