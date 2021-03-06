import React from "react";
import { Query } from "react-apollo";
import FeedPresenter from "./FeedPresenter";
import { GET_FEED } from "./FeedQueries";

class FeedQuery extends Query {}

export default class extends React.Component {
  render() {
    return (
      <FeedQuery
        query={GET_FEED}
        variables={{ page: 0 }}
        fetchPolicy="cache-and-network"
      >
        {({ data, loading, error }) => (
          <FeedPresenter data={data} loading={loading} error={error} />
        )}
      </FeedQuery>
    );
  }
}
